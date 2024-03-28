viterbi.futil:
	fuse viterbi.fuse --lower -b calyx -o viterbi.futil

parse:
	node parse.js

convert-data: parse
	$(F2P_CONVERTOR) ./viterbi.in.double.json init 1 > viterbi.in.posit.json
	$(F2P_CONVERTOR) ./viterbi.in.posit.json transition 2 > viterbi.in.posit_1.json
	$(F2P_CONVERTOR) ./viterbi.in.posit_1.json emission 2 > viterbi.in.posit.json 

run: viterbi.futil convert-data
	fud e --to dat viterbi.futil -s verilog.data viterbi.in.posit.json > viterbi.output.int.json

clean:
	rm *.json viterbi.futil *.jpg

.PHONY=clean