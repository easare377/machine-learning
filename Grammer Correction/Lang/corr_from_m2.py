#code taken from https://www.cl.cam.ac.uk/research/nl/bea2019st/data/corr_from_m2.py

# Apply the edits of a single annotator to generate the corrected sentences.
def main():
    """
    this function stores the correct sentence line by line in as txt file with file name lang8.train.auto.bea19.m2
    """
    
    m2 = open("lang8.train.auto.bea19.m2").read().strip().split("\n\n")
    out = open("lang8.train.auto.bea19.txt", "w")
    # Do not apply edits with these error types
    skip = {"noop", "UNK", "Um"}
    
    for sent in m2:
        sent = sent.split("\n")
        cor_sent = sent[0].split()[1:] # Ignore "S "
        edits = sent[1:]
        offset = 0
        for edit in edits:
            edit = edit.split("|||")
            if edit[1] in skip: continue # Ignore certain edits
            coder = int(edit[-1])
            if coder != 0: continue # Ignore other coders
            span = edit[0].split()[1:] # Ignore "A "
            start = int(span[0])
            end = int(span[1])
            cor = edit[2].split()
            cor_sent[start+offset:end+offset] = cor
            offset = offset-(end-start)+len(cor)
        out.write(" ".join(cor_sent)+"\n")
        
main()

#preprocessing incorrect sentences

file1 = open("lang8.train.auto.bea19.m2","r")
s1 = file1.read()

each_sent = s1.split("\n\n")

incorrect = []
for i in range(len(each_sent)):
    temp = each_sent[i].split("\n")
    temp = temp[0]
    temp = temp.split(" ")
    temp = temp[1:]# ignore S
    temp = ' '.join(temp)
    incorrect.append(temp)
    
#preprocessing correct sentences

file2 = open("lang8.train.auto.bea19.txt","r")
s2 = file2.read()

correct = s2.split("\n")

# storing correct and incorrect sentence pair into dataframe
df = pd.DataFrame()
df["correct"] = correct
df["incorrect"] = incorrect

#store into csv file named data.csv
df.to_csv("data.csv",index=False)