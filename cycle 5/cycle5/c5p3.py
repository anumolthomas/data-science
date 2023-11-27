def gen_ngrams(text,WordsToCombine):
    words=text.split()
    output=[]
    for i in range(len(words) - WordsToCombine +1):
        output.append(words[i:i+ WordsToCombine])
    return output
print("Name:Anumol Thomas\nRoll No:22MCA011\nCourse Name:DATA SCIENCE LAB\nCourse Code:20MCA241\n")
x=gen_ngrams(
    text='Data Science Lab ',WordsToCombine=2
)
print(x)