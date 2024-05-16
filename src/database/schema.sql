CREATE TABLE IF NOT EXISTS t_itinerary (
    itinerary_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    destinasi_id    INTEGER NOT NULL,
    lokasi          VARCHAR(100),
    tanggal         DATE CHECK(tanggal IS strftime('%Y-%m-%d', tanggal)),
    waktu_mulai     TEXT CHECK(waktu_mulai IS strftime('%H:%M:%S', waktu_mulai)),
    waktu_selesai   TEXT CHECK(waktu_selesai IS strftime('%H:%M:%S', waktu_selesai)),
    biaya           INTEGER,
    transportasi    VARCHAR(100),
    catatan         VARCHAR(300),
    FOREIGN KEY (destinasi_id) REFERENCES t_destinasi(destinasi_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS t_destinasi (
    destinasi_id    INTEGER PRIMARY KEY AUTOINCREMENT,
    nama            VARCHAR(50),
    kategori        VARCHAR(10),
    tanggal_mulai   DATE CHECK(tanggal_mulai IS strftime('%Y-%m-%d', tanggal_mulai)),
    tanggal_selesai DATE CHECK(tanggal_selesai IS strftime('%Y-%m-%d', tanggal_selesai)),
    budget          INTEGER,
    tabungan        INTEGER
);

CREATE TABLE IF NOT EXISTS t_artikel (
    artikel_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    judul           VARCHAR(100),
    konten          VARCHAR(1000),
    penulis         VARCHAR(50),
    tanggal_rilis   DATE CHECK(tanggal_rilis IS strftime('%Y-%m-%d', tanggal_rilis))
);

INSERT INTO t_artikel (judul, konten, penulis, tanggal_rilis)
VALUES ('Unveiling Athens: Key Attractions You Cant Miss', 
        'Athens, the capital city of Greece, is a place of history and culture where the past comes alive and seamlessly blends with the present. In our article, we’re here to guide you through the top attractions of Athens without getting too complicated.We’ll show you the must-see spots, like the famous Acropolis with its ancient ruins, the charming streets of Plaka, and the breathtaking views from Mount Lycabettus. The Acropolis is like Athens’ superstar attraction, standing tall above the city. You can’t miss it! The main star here is the Parthenon, a massive ancient temple dedicated to the goddess Athena. It’s all marble with grand columns, which is truly impressive.',
        'Paloma Diamond',
        '2004-05-07');

INSERT INTO t_artikel (judul, konten, penulis, tanggal_rilis)
VALUES ('Travel Guide to Nicaragua, Central America', 
        'A land of lakes, active volcanoes and well preserved colonial towns, Nicaragua has some of the best roads in Central America making it easy to get around. Nicaragua boasts stunning natural landscapes, and a difficult history that has shaped its identity. It’s part of the Pacific Ring of Fire, a region characterized by intense volcanic and seismic activity. The country’s volcanic landscape is the result of the movement of tectonic plates beneath the Earth’s surface. There are 19 volcanoes with 7 still active. From ancient indigenous civilizations to Spanish conquests, political upheavals, and revolutionary movements, Nicaragua’s story is a tapestry woven with threads of resilience, struggle, and hope.  The 20th century was a particularly turbulent time but now all is calm again and it’s difficult to believe that this country was the scene of such violence.',
        'Ucup Surucup',
        '2018-12-04');

INSERT INTO t_artikel (judul, konten, penulis, tanggal_rilis)
VALUES ('A Weekend in Sunny Sacramento, California', 
        'California’s hot spots have traditionally been Los Angeles, San Francisco (my home town) and San Diego. Yet Sacramento, despite being California’s capital, doesn’t feature as highly on the tourist trail. I only live a two-hour drive from the city, yet until recently even I hadn’t visited.More fool me, because, as I discovered, Sacramento has plenty to offer for a weekend of fun and frivolity. Sacramento is located at the confluence of the American and Sacramento rivers, California’s largest river, which flows to San Francisco Bay. This made it a pivotal location for the 1849 Gold Rush, thus cementing Sacramento as a major commercial and political centre.',
        'Thea Josephine',
        '2024-03-09');

INSERT INTO t_artikel (judul, konten, penulis, tanggal_rilis)
VALUES ('Why People Love Travelling', 
        'There are numerous benefits to travelling if we think about it. The first one being, we get to meet new people. When you meet new people, you get the opportunity to make new friends. It may be a fellow traveller or the local you asked for directions.Moreover, new age technology has made it easier to keep in touch with them. Thus, it offers not only a great way to understand human nature but also explore new places with those friends to make your trip easy. Similar to this benefit, travelling makes it easier to understand people. You will learn how other people eat, speak, live and more. When you get out of your comfort zone, you will become more sensitive towards other cultures and the people.Another important factor which we learn when we travel is learning new skills. When you go to hilly areas, you will most likely trek and thus, trekking will be a new skill added to your list.',
        'Thea Josephine',
        '2022-03-10');
