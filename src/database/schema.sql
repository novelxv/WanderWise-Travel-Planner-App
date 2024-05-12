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
        'Athens, the capital city of Greece, is a place of history and culture where the past comes alive and seamlessly blends with the present. In our article, we’re here to guide you through the top attractions of Athens without getting too complicated.',
        'Paloma Diamond',
        '2004-05-07');

INSERT INTO t_artikel (judul, konten, penulis, tanggal_rilis)
VALUES ('9 Ways How Travel Can Improve Your Mental Health', 
        'Travel, often seen as an escape from the mundane, holds a deeper significance as a potent tool for enhancing mental health. Venturing into new territories and experiences goes beyond mere relaxation; it offers a powerful catalyst for mental rejuvenation.',
        'Ucup Surucup',
        '2018-12-04');

INSERT INTO t_artikel (judul, konten, penulis, tanggal_rilis)
VALUES ('Why Choose Montenegro for Your Family Vacation in 2024?', 
        'Planning your family getaway for 2024? Well, hold on to your hats because Montenegro is the hidden gem you’ve been searching for! Tucked away in Southeast Europe, this tiny country packs a big punch when it comes to stunning landscapes, friendly locals, and a whole lot of adventure.',
        'Thea Josephine',
        '2024-03-09');
