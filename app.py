import streamlit as st
import os

# --- 0. 系統配置 ---
st.set_page_config(
    page_title="Sakiciw - 香雞酒",
    page_icon="🍲",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- 1. CSS 視覺特效 (維持 Cyber-Amis 風格) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700;900&family=Noto+Sans+TC:wght@300;500;900&display=swap');

    /* 全局背景：午夜霓虹漸層 */
    .stApp {
        background-color: #050505;
        background-image: 
            radial-gradient(circle at 50% 0%, #2a0a18 0%, transparent 60%),
            radial-gradient(circle at 80% 80%, #1a1a2e 0%, transparent 50%);
        color: #fff;
        font-family: 'Noto Sans TC', sans-serif;
    }

    /* 隱藏預設元素 */
    header {visibility: hidden;}
    .block-container {padding-top: 2rem; padding-bottom: 5rem;}

    /* --- 標題區：霓虹發光特效 --- */
    .neon-title {
        font-family: 'Orbitron', sans-serif;
        font-size: 80px;
        font-weight: 900;
        text-align: center;
        color: #fff;
        text-transform: uppercase;
        text-shadow: 
            0 0 5px #fff,
            0 0 10px #fff,
            0 0 20px #FF4D00,
            0 0 40px #FF4D00,
            0 0 80px #FF4D00;
        margin-bottom: 10px;
        animation: flicker 3s infinite alternate;
    }
    
    .artist-tag {
        text-align: center;
        font-size: 24px;
        color: #00E5FF; /* Cyber Cyan */
        letter-spacing: 5px;
        margin-bottom: 50px;
        text-shadow: 0 0 10px #00E5FF;
        font-weight: 300;
    }

    /* --- 唱片旋轉動畫 --- */
    .vinyl-container {
        display: flex;
        justify_content: center;
        align-items: center;
        margin: 20px auto;
        width: 300px;
        height: 300px;
        border-radius: 50%;
        background: radial-gradient(circle, #111 10%, #333 11%, #000 100%);
        box-shadow: 0 0 30px rgba(255, 77, 0, 0.3);
        border: 2px solid #333;
        position: relative;
        animation: spin 10s linear infinite;
    }
    
    .vinyl-label {
        width: 100px;
        height: 100px;
        background: linear-gradient(135deg, #FF4D00, #FFD600);
        border-radius: 50%;
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%);
        display: flex;
        align-items: center;
        justify-content: center;
        font-weight: bold;
        color: #000;
        font-family: 'Orbitron';
    }

    /* --- 歌詞卡片：玻璃擬態 (Glassmorphism) --- */
    .lyrics-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        padding: 40px;
        margin: 20px 0;
        text-align: center;
        box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        transition: all 0.5s ease;
    }

    .lyrics-card:hover {
        border-color: #FF4D00;
        box-shadow: 0 0 20px rgba(255, 77, 0, 0.2);
        transform: scale(1.02);
    }

    .amis-text {
        font-size: 28px;
        font-weight: 700;
        line-height: 1.6;
        background: linear-gradient(90deg, #fff, #ccc);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 20px;
    }

    .zh-text {
        font-size: 18px;
        color: #8892b0;
        line-height: 1.8;
        font-weight: 300;
        border-top: 1px solid rgba(255,255,255,0.1);
        padding-top: 20px;
    }

    /* --- 關鍵字 Highlight --- */
    .highlight {
        color: #FF4D00;
        font-weight: bold;
        text-shadow: 0 0 10px rgba(255, 77, 0, 0.6);
    }

    /* --- 動畫 Keyframes --- */
    @keyframes spin { 100% { transform: rotate(360deg); } }
    @keyframes flicker {
        0%, 18%, 22%, 25%, 53%, 57%, 100% {
            text-shadow:
            0 0 4px #fff,
            0 0 11px #fff,
            0 0 19px #fff,
            0 0 40px #FF4D00,
            0 0 80px #FF4D00,
            0 0 90px #FF4D00,
            0 0 100px #FF4D00,
            0 0 150px #FF4D00;
        }
        20%, 24%, 55% { text-shadow: none; }
    }
    
    /* --- 音訊播放器美化 --- */
    .stAudio { width: 100%; margin-top: 20px; }
    </style>
""", unsafe_allow_html=True)

# --- 2. 內容區塊 ---

# 標題區
st.markdown('<div class="neon-title">SAKICIW</div>', unsafe_allow_html=True)
st.markdown('<div class="artist-tag">詞曲 / 演唱：MALIKAY</div>', unsafe_allow_html=True)

# 佈局：左側視覺(唱片)，右側歌詞
col1, col2 = st.columns([1, 1.5])

with col1:
    # 視覺中心：旋轉唱片
    st.markdown("""
        <div style="display:flex; justify-content:center; align-items:center; height:100%; flex-direction:column;">
            <div class="vinyl-container">
                <div class="vinyl-label">HOT<br>SOUP</div>
            </div>
            <br>
    """, unsafe_allow_html=True)
    
    # --- 音訊播放器 (已針對 .m4a 調整) ---
    audio_file = "sakiciw.m4a"  # 這裡改成了 .m4a
    
    if os.path.exists(audio_file):
        # format='audio/mp4' 是播放 m4a 的標準 MIME type
        st.audio(audio_file, format='audio/mp4') 
    else:
        st.error(f"⚠️ 找不到檔案：{audio_file}")
        st.info("請確認 'sakiciw.m4a' 已經上傳到與 app.py 同一個資料夾中。")
        
    # 氛圍描述
    st.markdown("""
        <div style="text-align:center; margin-top:30px; color:#aaa; font-size:14px;">
            <span style="color:#FF4D00">●</span> 溫暖 (Diheko) &nbsp;&nbsp;
            <span style="color:#00E5FF">●</span> 幸福 (Malemed) &nbsp;&nbsp;
            <span style="color:#FFD600">●</span> 香氣 (Fangsis)
        </div>
        </div>
    """, unsafe_allow_html=True)

with col2:
    # 歌詞展示區
    st.markdown("""
    <div class="lyrics-card">
        <div class="amis-text">
            Fengiw sako <span class="highlight">fangsis</span> a maledef i taliyok,<br>
            mirav'oy to <span class="highlight">kiciw</span> cecayay a kaysing.<br><br>
            o satada <span class="highlight">malemeday</span> a malemed,<br>
            osaka <span class="highlight">diheko</span> mahinom ko faloco' i kasienawan,<br>
            dada ! layapen ko cecay a kiciw a mikohaw.
        </div>
        <div class="zh-text">
            撒佈在四圍的香氣，來享受一碗香雞酒，<br>
            是最最美滿幸福的，<br>
            冷冷的氣侯裏溫暖安慰在心坎裡，<br>
            來喝吧！領受一碗香雞酒。
        </div>
    </div>
    """, unsafe_allow_html=True)

    # 互動按鈕
    if st.button("🔥 感受這碗湯的溫度 (Feel the Heat)"):
        st.balloons()
        st.markdown("""
            <div style="text-align:center; font-size:20px; color:#FF4D00; font-weight:bold; margin-top:10px; text-shadow: 0 0 10px #FF4D00;">
                溫暖直達心坎裡！ (Diheko!)
            </div>
        """, unsafe_allow_html=True)

# --- 3. 底部版權 ---
st.markdown("""
    <div style="text-align:center; margin-top:50px; color:#444; font-size:12px; border-top:1px solid #222; padding-top:20px;">
        MUSIC APP DESIGN © 2025 | SAKICIW PROJECT
    </div>
""", unsafe_allow_html=True)
