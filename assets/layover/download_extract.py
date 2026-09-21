import urllib.request,zlib,struct,csv,io,json,time,pathlib,collections
root=pathlib.Path('downloaded_extract'); root.mkdir(exist_ok=True); out=root/'source_bos_lax.csv'
u='https://www.kaggle.com/api/v1/datasets/download/dilwong/flightprices'
start=time.time(); counts=collections.Counter(); n=0; kept=0; size=0; stop=None
with urllib.request.urlopen(u,timeout=60) as r, out.open('w',newline='',encoding='utf-8') as f:
 h=r.read(30); v=struct.unpack('<4s5H3I2H',h); name=r.read(v[-2]); extra=r.read(v[-1]); assert v[3]==8
 dec=zlib.decompressobj(-15); buf=b''; writer=None
 while stop is None:
  block=r.read(262144)
  if not block: break
  size+=len(block); buf+=dec.decompress(block); lines=buf.split(b'\n'); buf=lines.pop()
  for line in lines:
   vals=next(csv.reader([line.decode('utf-8')]))
   if writer is None:
    cols=vals; writer=csv.writer(f); writer.writerow(cols); idx={c:i for i,c in enumerate(cols)}; continue
   row=dict(zip(cols,vals)); n+=1
   if row['searchDate']!='2022-04-16': stop=row['searchDate']; break
   counts[row['startingAirport']]+=1
   if (row['startingAirport'],row['destinationAirport']) in [('BOS','LAX'),('LAX','BOS')]: writer.writerow(vals); kept+=1
  if n//100000 != (n-len(lines))//100000: print('rows',n,'kept',kept,'compressed MB',round(size/1e6),flush=True)
  if size>200_000_000: raise RuntimeError('Safety cap reached before date boundary')
meta={'source_url':u,'source_dataset':'https://www.kaggle.com/datasets/dilwong/flightprices','zip_member':name.decode(),'search_date':'2022-04-16','selection':'BOS-LAX or LAX-BOS, initial contiguous search-date block','rows_scanned_including_boundary':n,'next_search_date':stop,'rows_retained':kept,'compressed_bytes_read':size,'origin_counts':dict(counts),'elapsed_seconds':time.time()-start}
(root/'extraction.json').write_text(json.dumps(meta,indent=2)); print(json.dumps(meta,indent=2))
