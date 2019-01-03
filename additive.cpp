#include <bits/stdc++.h>
using namespace std;
bool isUppercase(char ch){
      return 'A'<=ch && ch<='Z';
}
string additiveCipher(string input,int key,bool isEncryption){
    
    string result;
    
    for (unsigned int i = 0; i < input.size(); i += 1)
    {
       char temp=input[i];
       if(temp!=' '){
        if(isUppercase(temp)){
          if(isEncryption)
          temp=(temp-'A'+key)%26;
          else
          temp=(temp-'A'-key)%26;
          
          temp+='A';
        }else{
          if(isEncryption)
          temp=(temp-'a'+key)%26;
          else
          temp=(temp-'a'-key)%26;
          
          temp+='a';
        }
       }
       result+=temp;
    }
    
    return result;
    
    
}
int main (int argc, char const* argv[])
{
	string plainText,cipherText;
	int key;
	cout<<"::ADDTIVIE CYPHER::\n";
        cout<<"Enter the plainText\n";
        getline(cin,plainText);
        cout <<"Enter the key\n";
        cin >> key;
        cout << "Encrypting the message..\n";
        cipherText = additiveCipher(plainText,key,true);
        cout <<"Encrypted message:"<<cipherText;
        cout <<"\nPress any key to decrypt the message";
        do
        {
        	char ch;
        	cin >> ch;
        } while (cin.peek()!=10);
        cout <<"Decrypted message:"<<additiveCipher(cipherText,key,false);
	return 0;
}

