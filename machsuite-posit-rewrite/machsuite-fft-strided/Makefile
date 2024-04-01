F2PConvertor=../../utilities/cpp/build/f2p_convertor
P2FConvertor=../../utilities/cpp/build/p2f_convertor

all: parse run convert-p2f-actual plot

%.futil: %.fuse
	fuse $< --lower -b calyx -o $@

convert-input:
	$(F2PConvertor) fft.in.double.json 32 --1d rel,img,img_twid,rel_twid > fft.in.posit.json

convert-p2f-actual:
	$(P2FConvertor) fft.out.posit.json 32 --1d rel,img,img_twid,rel_twid > fft.out.double.json

parse: check.data input.data
	node parse.js

run: fft.futil convert-input
	fud e --to dat $< -s verilog.data fft.in.posit.json --through verilog > fft.out.posit.json

plot:
	python plot.py

clean:
	rm *.json fft.futil *.jpg

.PHONY=parse clean convert-input convert-p2f-actual
