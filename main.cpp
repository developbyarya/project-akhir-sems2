#include <iostream>
#include <fstream>
#include <algorithm>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <dirent.h>



namespace py = pybind11;

using namespace std;

const char *lirik_folder = "lirik/";

DIR *dir;
struct dirent *ent;



string toLower(const string &str) {
    string lowerStr = str;
    transform(lowerStr.begin(), lowerStr.end(), lowerStr.begin(), ::tolower);
    return lowerStr;
}//deklarasi agar program menjadi insensitive//

vector<string> cariLirik(const string &cari) {
    bool ditemukan = false;
    int i = 0;
    vector<string> result;
    string judul;
    string cariLower = toLower(cari); //mengubah agar pencarian menjadi insensitive//
    dir = opendir(lirik_folder);

    if (dir != nullptr){
      const char *skip1 = ".";
      const char *skip2 = "..";
      while ((ent = readdir(dir)) != nullptr){
	if (strcmp(skip1, ent->d_name) && strcmp(skip2, ent->d_name) ) {
	// rekursif untuk mengecek semua file yang ada/
	  ifstream MyFile("lirik/" + string(ent->d_name));
	  
	  if (MyFile.is_open()) {
	      string line;
	      while (getline(MyFile, line)) {
		  string lineLower = toLower(line); 
		  if (lineLower.find(cariLower) != string::npos) {
		    //jika pencarian ditemukan maka akan menampilkan seluruh lirik pada file tersebut//
		      MyFile.close();
		      judul = ent->d_name;
		      result.push_back(ent->d_name);
		      ditemukan = true;
		      break;
		  }
		  
	      }
	      MyFile.close();//menutup file//
	  }
	};
      }
      closedir(dir);
    }

    if (!ditemukan) {//jika pencarian tidak ditemukan//
      return result;
    }
    return result;
}

int total_lagu(){
  ifstream file("lagu.txt");

  int count = 0;
  if (file.is_open()){
    string text;
    while (getline(file, text)){
      count++;
    }
  }
  file.close();

  return count;
}

void ambil_semua_lagu(string *lagu){
  ifstream file("lagu.txt");
  string text;

  int i = 0;
  while (getline(file, text)){
    lagu[i] = text;
    i++;
  }

  file.close();
  
  
}

void sort(string data[], int n){
  for (int i=0; i < n-1; i++){
    for (int j=0; j < n-i-1; j++){
      if (toLower(data[j]) > toLower(data[j+1])){
	swap(data[j], data[j+1]);
      }
    }
  }
}

string cari_judul_sequential(string judul, string penyanyi=""){
  string target = toLower(judul) + " - " + toLower(penyanyi);
  py::print(target);
  int n = total_lagu();
  int l = 0, r = n-1, m = (l+r)/2; 
  string lagu[n];
  ambil_semua_lagu(lagu);
  py::print(lagu[0]);

  for (int i=0; i < n; i++){
    string lagu_lower = toLower(lagu[i]);

    py::print("Mengecek: " + lagu_lower);

    if (lagu_lower.find(target) != string::npos) return lagu[i];
  }

  return "";
}


string cari_judul_binary(string judul, string penyanyi){
  string target = judul + " - " + penyanyi;
  int n = total_lagu();
  int l = 0, r = n-1, m = (l+r)/2; 
  string lagu[n];
  ambil_semua_lagu(lagu);
  sort(lagu, n);

  while (l <= r){
    if (target == lagu[m]) return lagu[m];
    else if (lagu[m] > target){
      l = m+1;
      m = (l+r)/2;
    } else {
      r = m - 1;
      m = (l+r) / 2;
    }

  }

  return "";

} 


string ambil_lirik(string judul){
  ifstream file("lirik/" + judul);
  string hasil = "";

  if (file.is_open()){
    string text;
    while (getline(file, text)){
      hasil += text + "\n";
    }
  }

  file.close();
  return hasil;
}



void tambahLagu(string judul, string lirik){
  ofstream file_judul("lagu.txt", ios::app);
  file_judul << judul << endl;
  file_judul.close();
  
  ofstream file_lirik("lirik/" + judul + ".txt");
  file_lirik << lirik << endl;
  file_lirik.close();
}

int main() {
    string lirik;
    cout << "Masukkan Lirik: ";
    getline(cin, lirik);
    cariLirik(lirik);
    return 0;
}


PYBIND11_MODULE(cpp, handle){
  handle.doc() = "Find songs and lyrics!";

  handle.def("tambah_lagu", &tambahLagu);

  handle.def("cari_by_lirik", &cariLirik);

  handle.def("ambil_lirik", &ambil_lirik);

  handle.def("cari_judul_sequential", &cari_judul_sequential);
  handle.def("cari_judul_binary", &cari_judul_binary);

}





