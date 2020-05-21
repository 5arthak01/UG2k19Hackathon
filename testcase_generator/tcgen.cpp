#include<iostream>
#include<algorithm>
#include<random>
#include<cstdint>

using namespace std;

#define ll int64_t

random_device rd;
mt19937_64 gen(rd());

ll rndm(ll min, ll max)
{
	uniform_int_distribution<ll> dis(min, max);
	return dis(gen);
}

int main()
{
	//fast I/O
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	ll t=-1, i=0, numtc=1, j=0, tmax=1, tmin=1;
	string sl;

	cout<<"How many sets of test cases do you want?"<<endl; fflush(NULL);
	cin>>numtc;

	cout<<"Are there multiple test cases?\nEnter yes or no:"<<endl; fflush(NULL);
	cin>>sl;
	transform(sl.begin(), sl.end(), sl.begin(), ::tolower);
	if(sl=="yes")
	{
		cout<<"Enter the minimum and maximum number of test cases:"<<endl; fflush(NULL);
		cin>>tmin>>tmax;
	}

	ll n=1;
	cout<<"Enter the number of variables on the first line:"<<endl; fflush(NULL);
	cin>>n;

	ll *arr = new ll[n];
	ll *arrmax = new ll[n];
	ll *arrmin = new ll[n];

	for(i=0;i<n;i++)
	{
		cout<<"Enter the minimum and maximum for variable "<<(i+1)<<endl; fflush(NULL);
		cin>>arrmin[i]>>arrmax[i];
	}

	ll m=0;
	cout<<"Enter the variable number on which decides the number of lines that follow:"<<endl; fflush(NULL);
	cin>>m;
	m--;


	ll k=1;
	cout<<"Enter the number of entries on each line:"<<endl; fflush(NULL);
	cin>>k;

	ll *line = new ll[k];
	ll *linemax = new ll[k];
	ll *linemin = new ll[k];

	for(i=0; i<k; i++)
	{
		cout<<"Enter the minimum and maximum for entry "<<(i+1)<<endl; fflush(NULL);
		cin>>linemin[i]>>linemax[i];
	}

	while(numtc--)
	{
		//check if there are multiple TCs
		if(t!=-1)
		{
			t=rndm(tmin, tmax);
			//append t
			cout<<t<<endl;
		}
		else
		{t=1;}
		while(t--)
		{
			//append the first line
			for(i=0;i<n;i++)
			{
				arr[i] = rndm(arrmin[i], arrmax[i]);
				cout<<arr[i]<<" ";
			}
			cout<<endl;

			//append each of the next arr[m] lines
			for(i=0;i<arr[m];i++)
			{
				//each line has k entries
				for(j=0; j<k; j++)
				{
					line[i] = rndm(linemin[i], linemax[i]);
					cout<<line[i]<<" ";
				}
				cout<<endl;
			}
		}
	}

	delete arr;
	delete arrmin;
	delete arrmax;
	delete line;
	delete linemin;
	delete linemax;

	return 0;
}
