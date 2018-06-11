from pandas_datareader import wb
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('ggplot')

print('Nation code:')
n = input()
print('from (year): ')
y1 = int(input())
print('to: ')
y2 = int(input())
#print(wb.search('gdp.*capita.*const').iloc[:,:2])

print('RESULT: ')
dat = wb.download(indicator='NY.GDP.PCAP.KD', country=[n], start=y2,end=y1)
print(dat)
dat['NY.GDP.PCAP.KD'].plot()
plt.xlabel('Year')
plt.ylabel('$')
plt.title('GDP')
plt.legend()
plt.show()