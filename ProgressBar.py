import time

from progress.bar import Bar #pip install progress

bar = Bar('Processing', max=20, suffix='%(index)d/%(max)d - %(percent).1f%% - %(eta)ds')
for i in range(20):
    time.sleep(.05) 
    bar.next()
bar.finish()
