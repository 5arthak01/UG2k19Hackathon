#include<iostream>
#include<fstream>
#include<algorithm>
#include<random>
#include<string>
#include<cstdint>
#include<cstdio>
#include<cstdlib>

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

	for(i=0;i<k;i++)
	{
		cout<<"Enter the minimum and maximum for entry "<<(i+1)<<endl; fflush(NULL);
		cin>>linemin[i]>>linemax[i];
	}

	//filesarr contains the name of test files that are to be created
	string *filesarr = new string[numtc+2];
	for(i=1; i<=numtc; i++)
	{
		filesarr[i] = "test"+to_string(i)+".txt";
	}

	FILE *file;

	for(ll loopvar=1; loopvar<=numtc; loopvar++)
	{
		char char_arr[filesarr[loopvar].length()];
		filesarr[loopvar].copy(char_arr, filesarr[loopvar].length(), 0);

		file = fopen(char_arr, "w");
		fclose(file);
		//if(file==NULL) ?
		//fprintf(file, ""); //clear the file
		file = fopen(char_arr, "a");

		//check if there are multiple TCs
		if(t!=-1)
		{
			t=rndm(tmin, tmax);
			//append t
			fprintf(file, "%I64d\n",t);
			//cout<<t<<endl;
		}
		else
		{t=1;}
		while(t--)
		{
			//append the first line
			for(i=0;i<n;i++)
			{
				arr[i] = rndm(arrmin[i], arrmax[i]);
				fprintf(file, "%I64d ",arr[i]);
				//cout<<arr[i]<<" ";
			}
			fprintf(file, "\n");
			//cout<<endl;

			//append each of the next arr[m] lines
			for(i=0;i<arr[m];i++)
			{
				//each line has k entries
				for(j=0; j<k; j++)
				{
					line[i] = rndm(linemin[i], linemax[i]);
					fprintf(file, "%I64d ",line[i]);
					//cout<<line[i]<<" ";
				}
				fprintf(file, "\n");
				//cout<<endl;
			}
		}
		fclose(file);
	}

	delete arr;
	delete arrmin;
	delete arrmax;
	delete line;
	delete linemin;
	delete linemax;
	delete filesarr;

	return 0;
}
