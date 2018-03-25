#!/usr/bin/env python
import json
import os

def fastp2table(jsons):
    '''convert jsons to tsv

    Args:
        jsons (list) :  has `jsons`

    Returns:
        dict: fastpTable 

    '''

    out = "fastqInfo.tsv" 
    fpw = open(out,"w")
    head = "\t".join(["sample","total_reads","total_bases","q20_rate","q30_rate","gc_content"]) + "\n"
    fpw.write(head)
    for js in jsons:
        sample = js.rstrip(".json")
        sample = sample.split("/")[-1]
        fp = open(js)
        jd = json.loads(fp.read())
        info = jd["summary"]["before_filtering"]
        reads = info["total_reads"]
        bases = info["total_bases"]
        q20 = info["q20_rate"]
        q30 = info["q30_rate"]
        gc = info["gc_content"]
        line = "\t".join( [str(item) for item in [sample,reads,bases,q20,q30,gc]]) + "\n"
        fpw.write(line)
    fpw.close()
    return out

if __name__ == "__main__":
    import sys
    js = sys.argv[1:]
    fastp2table(js)


