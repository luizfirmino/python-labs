#
# Luiz Filho
# 3/23/2021
# Module 6 Assignment
# 7. Write a program that takes your full name as input and displays the 
# abbreviations of the middle name except the first and last name which 
# is displayed as it is. 
# For example, if your name is Elvis Aaron Presley, then the output should be Elvis A. Presley.

famous_list = ''' \
Marilyn Monroe (1926 – 1962) American actress, singer, model
Abraham Lincoln (1809 – 1865) US President during American civil war
Nelson Mandela (1918 – 2013)  South African President anti-apartheid campaigner
John F. Kennedy (1917 – 1963) US President 1961 – 1963
Martin Luther King (1929 – 1968)  American civil rights campaigner
Queen Elizabeth II (1926 – ) British monarch since 1954
Winston Churchill (1874 – 1965) British Prime Minister during WWII
Donald Trump (1946 – ) Businessman, US President.
Bill Gates (1955 – ) American businessman, founder of Microsoft
Muhammad Ali (1942 – 2016) American Boxer and civil rights campaigner
Mahatma Gandhi (1869 – 1948) Leader of Indian independence movement
Margaret Thatcher (1925 – 2013) British Prime Minister 1979 – 1990
Mother Teresa (1910 – 1997) Macedonian Catholic missionary nun
Christopher Columbus (1451 – 1506) Italian explorer
Charles Darwin (1809 – 1882) British scientist, theory of evolution
Elvis Presley (1935 – 1977) American musician
Albert Einstein (1879 – 1955) German scientist, theory of relativity
Paul McCartney (1942 – ) British musician, member of Beatles
Queen Victoria ( 1819 – 1901) British monarch 1837 – 1901
Pope Francis (1936 – ) First pope from the Americas
'''

searchKey = input("Please Enter the name of the famous individual ? ")

if famous_list.upper().find(searchKey.upper()) > -1:
    print("Yup, " + searchKey + " did make the Top 20 cut!")
else:
    print("Sorry, " + searchKey + " did not make the Top 20 cut!")
