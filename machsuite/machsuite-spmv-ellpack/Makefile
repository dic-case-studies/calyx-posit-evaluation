F2P_CONVERTOR = ~/Documents/projects/posit-git-tw/hardposit-chisel3/test_generator/build/F2PConvertor
P2F_CONVERTOR = ~/Documents/projects/posit-git-tw/hardposit-chisel3/test_generator/build/P2FConvertor

spmv.futil:
	fuse ./spmv.fuse --lower -b calyx -o spmv.futil

test_data:
	$(F2P_CONVERTOR) ./input.double.fuse.data nzval 2 > input.posit.fuse.data
	$(F2P_CONVERTOR) ./input.posit.fuse.data vec 1 > input.fuse.data 

run: spmv.futil test_data
	fud e --to dat spmv.futil -s verilog.data input.fuse.data > output.posit.fuse.data

benchmark: run
	$(P2F_CONVERTOR) ./output.posit.fuse.data out 1 > output.double.fuse.data
	python3 plot.py

clean:
	rm *.fuse.data spmv.futil *.jpg

.PHONY=clean