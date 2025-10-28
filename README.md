# 매치업: NLP
매치업 Python을 사용한 자연어 처리 심화 교육자료

# 🗣️ PyQt5 Speech Transcriber
> PyQt5 GUI에서 `speech_recognition`으로 마이크 음성을 텍스트로 변환하는 간단한 예제 앱

## 📖 소개
이 애플리케이션은 `PyQt5` 기반 GUI에서 버튼으로 **음성 인식 시작/정지**를 제어하고,
인식된 텍스트를 실시간으로 화면에 표시합니다.  
백엔드는 `speech_recognition` 라이브러리를 사용합니다.

---

## 💻 Python 가상환경 설정

### 1️⃣ 가상환경 생성
#### 🪟 Windows
```bash
python -m venv venv
```
#### 🍎 macOS / 🐧 Linux
```bash
python3 -m venv venv
```

### 2️⃣ 가상환경 활성화
#### 🪟 Windows
```bash
venv\Scripts\activate
```
#### 🍎 macOS / 🐧 Linux
```bash
source venv/bin/activate
```

### 3️⃣ 패키지 설치
```bash
pip install -r requirements.txt
```
> Python 10.x.x버전 기반이며, 그 외 버전에서는 오류가 발생할 수 있습니다.
> 오류 발생 시 아래로 설치 바랍니다.
```bash
pip install jupyter SpeechRecognition PyQt5 pyinstaller
```

---

## ▶️ 실행
```bash
python main.py
```
앱이 실행되면 **Start** 버튼으로 인식을 시작하고 **Stop**으로 중지합니다.  
텍스트 박스에 인식 결과가 표시됩니다.

---

### 2) 기본 빌드 (콘솔 창 없는 GUI 모드)
#### 🪟 Windows
```bash
pyinstaller --onefile --windowed --name PyQtSpeechTranscriber --icon assets/app.ico main.py
```
생성물: `dist/PyQtSpeechTranscriber.exe`
> --onefile: 한개 파일로 나오도록 빌드합니다
> --windowed: 콘솔창을 표시하지 않습니다. (파이썬 내 print 등, 시스템메시지 확인불가)
> --name: 앱 이름을 설정합니다.
> --icon: 앱 아이콘을 설정합니다.

#### 🍎 macOS / 🐧 Linux
```bash
pyinstaller --onefile --windowed --name PyQtSpeechTranscriber --icon assets/app.icns main.py
```
생성물: `dist/PyQtSpeechTranscriber` (macOS의 경우 앱 번들을 원하면 `--onefile` 대신 `--name ... --windowed`만 주고 `.app` 생성)

### 3) 리소스(이미지/설정파일) 포함
- **경로 구분자 주의**: Windows는 `;`, macOS/Linux는 `:` 를 사용합니다.

#### 🪟 Windows
```bash
pyinstaller --onefile --windowed main.py   --add-data "docs\*;docs" --add-data "assets\*;assets"
```

#### 🍎 macOS / 🐧 Linux
```bash
pyinstaller --onefile --windowed main.py   --add-data "docs/*:docs" --add-data "assets/*:assets"
```

### 4) 음성 인식 관련 훅/히든 임포트(필요 시), (본 프로젝트 불필요)
일부 환경에서 `pyaudio` 또는 백엔드 관련 모듈 검색이 누락될 수 있습니다.
```bash
pyinstaller --onefile --windowed main.py   --hidden-import=pyaudio --hidden-import=speech_recognition
```
---

## 🧭 Git 기본 사용법

```bash
# 저장소 클론
git clone https://github.com/yourusername/pyqt5-speech-transcriber.git
cd pyqt5-speech-transcriber

# 새 브랜치 생성
git checkout -b feature/기능명

# 변경사항 커밋 및 푸시
git add .
git commit -m "Add: 기능 설명"
git push origin feature/기능명
```

---

## 📄 라이선스
이 프로젝트는 **GPL v3 (GNU General Public License)** 를 따릅니다.  
PyQt5는 GPL 라이선스(또는 상용 라이선스)로 배포되며, 본 예제는 GPL 조건하에 오픈소스로 공개됩니다.
