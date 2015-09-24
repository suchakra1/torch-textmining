
Torch based deep learning application in text mining using character level representations


It shows 98% classification accuracy using stackoverflow data. Also added option  for  a single int representation instead of binary vector for characters. 

Reference:
1 torch7 Collebert '11, Torch7, Deep Learning package, torch.ch, 
Needs CUDA 6, developer.nvidia.com/cuda-downloads

2. Original source Code : .github.com/zhangxiangxiao/Crepe

3. Data taken from Stack Exchange data,
blog.stackoverflow.com/2009/06/stack-overflow-creative-commons-data-dump/,
kaggle.com/c/facebook-recruiting-iii-keyword-extraction/data (CSV format)

selection.py selects training and test data subset
csv27b is a converter from lua to torch readable format
and lua config files  
