#include <iostream>
#include <cstring>
#include <dirent.h>
#include <fstream>

using namespace std;

void some(int *a){
  for (int i=0; i < 5; i++){
    a[i] = i+2;
  }
}


int main(){
  int arr[5];
  some(arr);

  cout << arr[1] << endl;
  
  return 0;

}
