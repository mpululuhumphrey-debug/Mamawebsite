from flask import Flask, render_template_string, url_for

app = Flask(__name__)

HTML = """
<!DOCTYPE html>
<html lang="sw">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Kwa Mama Yangu ❤️</title>

    <style>
        * { box-sizing: border-box; }

        body {
            margin: 0;
            min-height: 100vh;
            font-family: Arial, sans-serif;
            background: linear-gradient(135deg, #fff0f5, #ffe4e1, #fce7f3);
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 24px 15px;
            overflow-x: hidden;
        }

        .card {
            position: relative;
            z-index: 2;
            width: 100%;
            max-width: 480px;
            background: rgba(255,255,255,0.96);
            padding: 28px 22px;
            border-radius: 24px;
            text-align: center;
            box-shadow: 0 12px 35px rgba(150,50,90,0.18);
            animation: cardAppear 1.2s ease;
        }

        .mama-photo {
            width: 180px;
            height: 180px;
            object-fit: cover;
            border-radius: 50%;
            border: 5px solid #ffe0eb;
            box-shadow: 0 5px 20px rgba(194,24,91,0.2);
            display: block;
            margin: 0 auto 18px;
        }

        .decoration {
            font-size: 30px;
            margin-bottom: 8px;
        }

        h1 {
            color: #c2185b;
            font-size: 27px;
            margin: 10px 0 14px;
        }

        .intro {
            color: #79515f;
            font-size: 16px;
            line-height: 1.8;
        }

        button {
            background: linear-gradient(135deg, #e91e63, #ad1457);
            color: white;
            border: none;
            padding: 14px 22px;
            border-radius: 30px;
            font-size: 16px;
            font-weight: bold;
            margin-top: 18px;
            cursor: pointer;
            box-shadow: 0 5px 15px rgba(194,24,91,0.2);
        }

        button:active {
            transform: scale(0.96);
        }

        #message {
            display: none;
            text-align: left;
            color: #49313b;
            font-size: 16px;
            line-height: 1.9;
            margin-top: 22px;
        }

        #message.show {
            display: block;
            animation: revealMessage 3s ease both;
        }

        @keyframes revealMessage {
            from {
                opacity: 0;
                transform: scale(0.94);
                clip-path: inset(50%);
            }
            to {
                opacity: 1;
                transform: scale(1);
                clip-path: inset(0);
            }
        }

        .signature {
            text-align: center;
            color: #c2185b;
            font-weight: bold;
            margin-top: 22px;
        }

        .heart {
            font-size: 30px;
            animation: heartbeat 1s infinite;
        }

        .music-button {
            background: #fff0f5;
            color: #ad1457;
            border: 1px solid #f8bbd0;
            box-shadow: none;
            display: block;
            margin: 10px auto;
        }

        .falling-flower {
            position: fixed;
            top: -50px;
            z-index: 1;
            pointer-events: none;
            animation: flowerFall linear forwards;
        }

        @keyframes cardAppear {
            from { opacity: 0; transform: translateY(25px); }
            to { opacity: 1; transform: translateY(0); }
        }

        @keyframes heartbeat {
            50% { transform: scale(1.2); }
        }

        @keyframes flowerFall {
            0% { transform: translateY(0) rotate(0deg); opacity: 0; }
            10% { opacity: 0.9; }
            100% { transform: translateY(110vh) rotate(360deg); opacity: 0; }
        }

        @media(max-width:380px) {
            .card { padding: 22px 16px; }
            .mama-photo { width: 150px; height: 150px; }
            h1 { font-size: 23px; }
        }
    </style>
</head>

<body>

<audio id="myMusic" loop preload="none">
    <source src="{{ url_for('static', filename='mama.mp3') }}"
            type="audio/mpeg">
</audio>

<main class="card">

    <img
        src="{{ url_for('static', filename='mama.jpg') }}"
        alt="Mama yangu mpendwa"
        class="mama-photo"
        onerror="this.style.display='none';
        document.getElementById('imageError').style.display='block';">

    <p id="imageError" style="display:none;color:#c2185b;">
        Picha haijapatikana. Tafadhali hakiki faili mama.jpg
    </p>

    <div class="decoration">💐🌹💐</div>

    <h1>Kwa Mama Yangu Mpendwa ❤️</h1>

    <p class="intro">
        Mama, nimekuandalia ujumbe maalumu kutoka moyoni mwangu.
        Natumaini utakufurahisha. ❤️
    </p>

    <button id="openButton" onclick="openMessage()">
        💌 Fungua Ujumbe Wako
    </button>

    <button class="music-button" id="musicButton"
            onclick="toggleMusic()">
        🎵 Washa Muziki
    </button>

    <p id="musicError" style="display:none;color:#c2185b;">
        Muziki haujapatikana. Hakiki faili mama.mp3
    </p>

    <div id="message">

        <p><strong>Mama yangu mpendwa! ❤️</strong></p>

        <p>
            Kama kuna zawadi moja ambayo Mungu amenipa na
            nitashukuru milele, basi ni kuwa na wewe kama
            mama yangu. Hakuna maneno yanayoweza kueleza
            kikamilifu jinsi ninavyokupenda na kukuthamini.
        </p>

        <p>
            Asante kwa upendo wako, kwa kunijali, kwa
            kunivumilia na kwa kila jambo ulilofanya kwa
            ajili yangu. Hata kama wakati mwingine nashindwa
            kukuambia ninavyokupenda, nataka ujue kwamba
            nafasi yako moyoni mwangu haiwezi kuchukuliwa
            na mtu mwingine yeyote.
        </p>

        <p>
            Mama, wewe ni baraka katika maisha yangu.
            Ninakuombea Mungu akupe afya njema, amani,
            furaha na maisha marefu. Akulinde kila siku
            na akujalie kuona matunda ya juhudi zako.
        </p>

        <p>
            Natamani siku moja nikupe sababu nyingi za
            kutabasamu na ujivunie kuwa na mimi kama
            mtoto wako.
        </p>

        <p>
            Huenda nisiwe na kila kitu duniani, lakini
            ninashukuru kwa kuwa na wewe. Upendo wako ni
            zawadi ambayo siwezi kuilinganisha na kitu
            chochote.
        </p>

        <p><strong>MAMA, NAKUPENDA SANA! ❤️</strong></p>

        <p>
            Mungu akubariki, mama yangu. Akupe nguvu,
            afya njema na furaha tele. 🙏🌹
        </p>

        <div class="signature">
            Kwa upendo mwingi,<br>
            Mtoto wako anayekupenda ❤️
            <div class="heart">💖</div>
        </div>

    </div>

</main>

<script>

    function openMessage() {
        const message = document.getElementById("message");
        const button = document.getElementById("openButton");

        message.classList.remove("show");
        void message.offsetWidth;
        message.classList.add("show");

        button.style.display = "none";

        setTimeout(function() {
            message.scrollIntoView({
                behavior: "smooth",
                block: "nearest"
            });
        }, 100);
    }

    const flowerTypes = ["🌹", "🌸", "🌺", "🌷", "💗"];

    function createFlower() {
        const flower = document.createElement("div");

        flower.className = "falling-flower";
        flower.textContent =
            flowerTypes[Math.floor(Math.random() * flowerTypes.length)];

        flower.style.left = Math.random() * 100 + "vw";
        flower.style.fontSize = (16 + Math.random() * 14) + "px";

        const duration = 7 + Math.random() * 5;
        flower.style.animationDuration = duration + "s";

        document.body.appendChild(flower);

        setTimeout(function() {
            flower.remove();
        }, duration * 1000);
    }

    setInterval(createFlower, 1200);

    async function toggleMusic() {

        const music = document.getElementById("myMusic");
        const button = document.getElementById("musicButton");
        const errorMessage = document.getElementById("musicError");

        if (music.paused) {

            try {
                await music.play();

                button.textContent = "⏸️ Simamisha Muziki";
                errorMessage.style.display = "none";

            } catch (error) {

                errorMessage.style.display = "block";
                button.textContent = "🎵 Jaribu Tena";
            }

        } else {

            music.pause();
            button.textContent = "🎵 Washa Muziki";

        }
    }

</script>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
