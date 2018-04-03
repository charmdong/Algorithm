#include <iostream>
#include <set>
#include <vector>
#include <string>
using namespace std;

void res(vector<string> v);

int main()
{
	vector<string> v;
	string tmp;
	
	while (1) {
		cin >> tmp;
		if (tmp == ".")
			break;
		v.push_back(tmp);
	}
	res(v);
	return 0;
}

void res(vector<string> v)
{
	set<char> s;
	
	for (int i = 0; i < v.size(); i++) {
		for (int j = 0; j < v[i].length(); j++)
			s.insert(v[i][j]);
		cout << v[i].length() / s.size() << endl;
		s.clear();
	}
}