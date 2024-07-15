from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from dbTB2 import conn


app = FastAPI()


# Model Pydantic untuk mendefinisikan skema data Buku
class Buku(BaseModel):
    id: Optional[int] = None
    judul: str
    penulis: str
    penerbit: str
    tahun_terbit: int
    konten: List[str]
    iktisar: str


# Untuk membuat buku
@app.post("/buku/", response_model=Buku)
def create_buku(buku: Buku):
    cursor = conn.cursor()
    sql = "INSERT INTO buku (judul, penulis, penerbit, tahun_terbit, konten, iktisar) VALUES (%s, %s, %s, %s, %s, %s)"
    val = (buku.judul, buku.penulis, buku.penerbit, buku.tahun_terbit, buku.konten, buku.iktisar)
    cursor.execute(sql, val)
    conn.commit()
    buku.id = cursor.lastrowid
    cursor.close()
    return buku


# Untuk membaca buku
@app.get("/buku/{buku_id}", response_model=Buku)
def read_buku(buku_id: int):
    cursor = conn.cursor()
    query = "SELECT id, judul, penulis, penerbit, tahun_terbit, konten, iktisar FROM buku WHERE id=%s"
    cursor.execute(query, (buku_id,))
    item = cursor.fetchone()
    cursor.close()
    if item is None:
        raise HTTPException(status_code=404, detail="Buku tidak ditemukan")
    return Buku(
        id=item[0],
        judul=item[1],
        penulis=item[2],
        penerbit=item[3],
        tahun_terbit=item[4],
        konten=item[5].splitlines(),
        iktisar=item[6]
    )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8080)
