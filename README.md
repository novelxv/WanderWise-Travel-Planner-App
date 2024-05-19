# WanderWise: Wise Up Your Wanderlust

## Overview

Wanderwise is a travel planner desktop software application. Wanderwise also provides a collection of articles related to travelling. Users of this application can see, add, edit, and delete the destination along with its itineraries and details. Users can also track their budget progress throughout their travelling plan.

## Set up
- clone this repository using command
```
git clone https://gitlab.informatika.org/novelxv/if2250-2024-k02-g11-wanderwise.git
```
1. install requirements with
```
pip install requirements.txt
```
2. install all packages
```
pip install -e .
```
3. Run the program from root directory using
```
python src/main.py
```

## Testing (optional)
To test if the database is correctly initialized, run unit tests with the following command from the `tests` repository.
```
pytest
```

## How to use

## Features


## Database Structure

1. Articles

|     Field     |    Type   | NULL |   Key   |       Extra      |
| ------------- |  -------- | ---- | ------- | ---------------- |
| artikel_id    |  INTEGER  |  NO  |   PRI   |  auto_increment  |
| judul         |    TEXT   |  NO  |         |                  |
| konten        |    TEXT   |  NO  |         |                  |
| penulis       |    TEXT   |  NO  |         |                  |
| tanggal_rilis |    DATE   |  NO  |         |                  |

2. Destinations

|       Field     |    Type   | NULL |   Key   |       Extra      |
| --------------- |  -------- | ---- | ------- | ---------------- |
| destinasi_id    |  INTEGER  |  NO  |   PRI   | auto_increment   |
| nama            |    TEXT   |  NO  |         |                  |
| kategori        |    TEXT   |  NO  |         |                  |
| tanggal_mulai   |    DATE   |  NO  |         |                  |
| tanggal_selesai |    DATE   |  NO  |         |                  |
| budget          |  INTEGER  |  NO  |         |                  |
| tabungan        |  INTEGER  |  NO  |         |                  |

3. Itinerary

|       Field     |    Type   | NULL |   Key   |                 Extra              |
| --------------- |  -------- | ---- | ------- | ---------------------------------  |
| itinerary_id    |  INTEGER  |  NO  |   PRI   |            auto_increment          |
| destinasi_id    |  INTEGER  |  NO  |         |REFERENCES t_destinasi(destinasi_id)|
|     tanggal     |    DATE   |  NO  |         |                                    |
|  waktu_mulai    |    TIME   |  NO  |         |                                    |
|     lokasi      |    TEXT   |  NO  |         |                                    |
| waktu_selesai   |    TIME   |  NO  |         |                                    |
|     biaya       |  INTEGER  |  NO  |         |                                    |
|  transportasi   |    TEXT   |  NO  |         |                                    |
|    catatan      |    TEXT   |  NO  |         |                                    |

## Contributors
|         Name           |     NIM    | Contribution |  
| ---------------------- |  --------- | ------------ | 
| Novelya Putri Ramadhani|  13522096  | Destination, some component and pages, testing            |   
|   Kayla Namira Mariadi |  13522050  | Database, controller, form box component, testing             |   
|    Saad Abdul Hakim    |  13522092  | Management Form, some component and pages, testing             |   
| Diana Tri Handayani    |  13522104  | Budgeting, Empty Pages,  some component and pages, testing            |   
| Thea Josephine Halim   |  13522012  | Management Itinerary, some component and pages, testing          |   
| Zulkifli Ardiansyah    |  10023640  | Halaman Utama, Manajemen Artikel, and some component, testing             |      