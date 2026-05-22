## EduQUest 
EduQuest adalah platform education dengan gamingfikasi, dimana user bermain sambil belajar
gamingfikasi yang dihadirkan adalah bertipe RPG dimana pemain menjawab soal untuk mengalahkan monster dan memiliki level kesulitan untuk tiap level
kita juga menghadirkan ai chatbot (project kita kali ini yang akan kita kembangkan) dimana dia adalah mentor kita untuk membahas soal dan juga bisa kita tanya jawab untuk membantu kita menjawab soal. nama chatbotnya ada Lex (dia adalah seorang dinosaurus (T-rex))


## Seputar project ini tentang apa
Saya membuat ai model untuk chatbot yang terhubung ke front end (vue.js) dan backend (laravel).

## ALur program 
Vue
↓
POST /chat ke Laravel
↓
Laravel cek user login
↓
Laravel simpan pesan user
↓
Laravel POST ke FastAPI
↓
FastAPI kirim prompt ke Groq/OpenAI
↓
LLM generate jawaban
↓
FastAPI return jawaban
↓
Laravel simpan jawaban AI
↓
Laravel return ke Vue
↓
Vue tampilkan chat

## Chatbot 
chatbot ini adalah chatbot untuk user bisa tanya jawab dengannya dan juga bisa memberikan saran dan rekomendasi seputar soal yang dikerjakan, jadi Lex harus tau user sedang mengerjakan apa dan harus tau juga soal yang dikerjakan apa agar ketika user bertanya tidak perlu kasih tau soalnya jadi cukup bilang kesusahan aja maka lex pun sudah tau harus membantu apa 

## Apa yang aku mau kamu lakukan 
- aku mau kamu mengembangkan project ini agar sesuai
- jika kamu ambigu atau bingung maka bertanya lah agar tidak terjadi kekeliruan saat melakukan code
- buat kodenya seefiesenmungkin dan tambahkan comment agar ada arahan apa yang kamu tulis dan penjelasan mengenai codenya

## Apa yang tidak boleh kamu lakukan 
- jangan buat file .md baru untuk membahas apapun, bahas saja di code menggunakan comment (#)
