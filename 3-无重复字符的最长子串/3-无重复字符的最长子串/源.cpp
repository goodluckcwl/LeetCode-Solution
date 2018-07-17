#include<string>
#include<set>
#include<iostream>
#include<assert.h>
#include<vector>
#include<memory.h>
using namespace std;

class Solution {
public:
	int lengthOfLongestSubstring(string s) {
		
		int index[256];
		for (int i = 0; i<256; ++i) {
			index[i] = -1;
		}
		int ans = 0;
		for (int i = 0, j = 0; j < s.size(); ++j) {
			// 查找字符是否出现过,如果映射出的下标大于i，说明出现过。
			int ch_idx = index[s[j]];
			i = ch_idx > i ? ch_idx : i;
			int length = j - i + 1;
			ans = ans > length? ans : length;
			index[s[j]] = j + 1;
		}
		return ans;
	}
private:

};

string stringToString(string input) {
	assert(input.length() >= 2);
	string result;
	for (int i = 1; i < input.length() - 1; i++) {
		char currentChar = input[i];
		if (input[i] == '\\') {
			char nextChar = input[i + 1];
			switch (nextChar) {
			case '\"': result.push_back('\"'); break;
			case '/': result.push_back('/'); break;
			case '\\': result.push_back('\\'); break;
			case 'b': result.push_back('\b'); break;
			case 'f': result.push_back('\f'); break;
			case 'r': result.push_back('\r'); break;
			case 'n': result.push_back('\n'); break;
			case 't': result.push_back('\t'); break;
			default: break;
			}
			i++;
		}
		else {
			result.push_back(currentChar);
		}
	}
	return result;
}
int main() {


	int ret = Solution().lengthOfLongestSubstring("abcabcbb");

	return 0;
}