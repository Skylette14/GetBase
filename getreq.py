import time
import requests
import re


url_head = "https://genome.ucsc.edu/cgi-bin/hgc?hgsid=870916183_ePqASqabI4QwiIi82oEhMn4vOnQF&c=chr13&"
url_last = "&g=multiz100way&i=multiz100way"

params = {"_ga":"GA1.2.1288351756.1590597380","_gid":"GA1.2.1691826421.1596434113","hguid.genome-japan":"676319865_OYgN0rmzfZa6aU1pBWc61IVP1fZS"}

def get_resp_first_page(unchecked_str):

	arr = unchecked_str.split(":")[-1]
	url = url_head + "l=" + str(int(arr)-1) + "&r=" + arr + "&o=" + str(int(arr)-1) + "&t=" + arr + url_last
	print(url)
	response = requests.get(url = url, params = params)
	key_pre = str(response.text).split("<PRE>")[1].split("</PRE>")[0]

	return key_pre

def keywords_handler(key_pre):
	map_key = []
	map_value = []
	result = dict()
	temp_arr = key_pre.split("\n")
	for i in range(len(temp_arr)):
		matchkey = re.findall(">(.*?)</A>", temp_arr[i].replace(" ",""))
		if matchkey is not None and len(matchkey) != 0:
			map_key.append(matchkey[-1])
		matchvalue = re.findall("</A>[AaCcTtGgNn=-]+", temp_arr[i].replace(" ",""))
		if matchvalue is not None and len(matchvalue) != 0:
			map_value.append(matchvalue[0].replace("</A>",""))
	if len(map_key) == len(map_value):
		for i in range(len(map_key)):
			result[map_key[i]] = map_value[i]
			#print(map_key[i],":",map_value[i])
		# print(result)

	return result



def get_result(unchecked_str):
	key_pre = get_resp_first_page(unchecked_str)
	result = keywords_handler(key_pre)

	return result


def main():
	#unchecked_str = "chr17:43067264"    #多个减号
	#unchecked_str = "chr17:43092194"
	unchecked_str = "chr17:43092719"
	# unchecked_str = "chr17:43114718"
	result = get_result(unchecked_str)
	'''TODO  加入后续操作   存入Excel'''
	# save_to_Excel(result)
	# print(result)


if __name__ == '__main__':
	main()
