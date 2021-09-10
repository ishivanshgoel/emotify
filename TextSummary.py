from pysummarization.nlpbase.auto_abstractor import AutoAbstractor
from pysummarization.tokenizabledoc.simple_tokenizer import SimpleTokenizer
from pysummarization.abstractabledoc.top_n_rank_abstractor import TopNRankAbstractor

class TextSummary():
    def __init__(self, data):
        self.document = data
    
    def getSummary(self):
        document = self.document
        auto_abstractor = AutoAbstractor()
        auto_abstractor.tokenizable_doc = SimpleTokenizer()
        auto_abstractor.delimiter_list = [".", "\n"]
        abstractable_doc = TopNRankAbstractor()
        result_dict = auto_abstractor.summarize(document, abstractable_doc)
        result = ""
        for sentence in result_dict["summarize_result"]:
            result += sentence
        return result
