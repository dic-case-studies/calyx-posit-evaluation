convert-data:
	$(F2PConvertor) fft.fuse.double.json rel > fft.fuse.posit_1.json 
	$(F2PConvertor) fft.fuse.posit_1.json img > fft.fuse.posit.json 
	$(F2PConvertor) fft.fuse.posit.json img_twid > fft.fuse.posit_1.json 
	$(F2PConvertor) fft.fuse.posit_1.json rel_twid > fft.fuse.posit.json

convert-expect:
	$(F2PConvertor) fft.expect.double.json rel > fft.expect.posit_1.json 
	$(F2PConvertor) fft.expect.posit_1.json img > fft.expect.posit.json 
	$(F2PConvertor) fft.expect.posit.json img_twid > fft.expect.posit_1.json 
	$(F2PConvertor) fft.expect.posit_1.json rel_twid > fft.expect.posit.json

convert-p2f-expect:
	$(P2FConvertor) fft.out.json rel > fft.out_1.json 
	$(P2FConvertor) fft.out_1.json img > fft.out.json 
	$(P2FConvertor) fft.out.json img_twid > fft.out_1.json 
	$(P2FConvertor) fft.out_1.json rel_twid > fft.out.json
