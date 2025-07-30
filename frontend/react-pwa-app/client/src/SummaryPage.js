// SummaryPage.js

import React from 'react';
import { useLocation, useNavigate } from 'react-router-dom';

export default function SummaryPage() {
  const location = useLocation();
  const navigate = useNavigate();
  const summaryText = location.state?.summary || '';

  const handleVoice = () => {
    if ('speechSynthesis' in window && summaryText) {
      const utter = new window.SpeechSynthesisUtterance(summaryText.replace(/\n/g, ' '));
      utter.lang = 'ko-KR';
      window.speechSynthesis.speak(utter);
    }
  };

  const handleBack = () => {
    navigate('/camera'); // 다시 찍기로 카메라 화면 이동
  };

  return (
    <div style={styles.page}>
      <div style={styles.container}>
        {/* 상단 검정바 */}
        <div style={styles.topBar}>
          <button style={styles.backBtn} onClick={handleBack}>&larr;</button>
          <span style={styles.topTitle}>다시 찍기</span>
        </div>

        {/* 요약 텍스트 */}
        <div style={styles.summaryWrap}>
          {summaryText
            ? summaryText.split('\n').map((line, idx) => (
                <div key={idx} style={styles.summaryText}>{line}</div>
              ))
            : <div style={{ color: '#aaa' }}>요약 결과가 여기에 표시됩니다</div>
          }
        </div>

        {/* 하단 버튼 */}
        <div style={styles.bottomBar}>
          <button style={styles.voiceButton} onClick={handleVoice}>
            <span role="img" aria-label="mic" style={styles.micIcon}>🎤</span>
            <span style={styles.voiceButtonText}>음성으로 질문하기</span>
          </button>
        </div>
      </div>
    </div>
  );
}

const styles = {
  page: {
    minHeight: '100vh',
    background: '#fff',
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
  },
  container: {
    width: 320,
    minHeight: '80vh',
    margin: '40px auto',
    border: '4px solid #eee',
    borderRadius: 18,
    background: '#fff',
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'space-between',
    alignItems: 'center',
    boxSizing: 'border-box',
    padding: '0 0 0 0',
    position: 'relative',
  },
  topBar: {
    height: 44,
    width: '100%',
    background: '#111',
    display: 'flex',
    alignItems: 'center',
    borderTopLeftRadius: 14,
    borderTopRightRadius: 14,
    marginBottom: 8,
    justifyContent: 'flex-start'
  },
  backBtn: {
    background: 'none',
    border: 'none',
    color: '#fff',
    fontSize: 22,
    marginLeft: 12,
    cursor: 'pointer',
    outline: 'none'
  },
  topTitle: {
    color: '#fff',
    fontSize: 16,
    fontWeight: 500,
    marginLeft: 7,
    letterSpacing: -1,
  },
  imageBox: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    width: '100%',
    marginTop: 12,
    marginBottom: 7,
  },
  previewImg: {
    width: 220,
    height: 140,
    objectFit: 'cover',
    borderRadius: 10,
    border: '1.5px solid #ccc',
    marginBottom: 7,
    background: '#eee'
  },
  zoomBtn: {
    border: 'none',
    borderRadius: 7,
    background: '#f8f8f8',
    color: '#333',
    padding: '4px 17px',
    fontSize: 14.5,
    fontWeight: 500,
    boxShadow: '0 1px 4px 0 rgba(0,0,0,0.06)',
    cursor: 'pointer',
    display: 'flex',
    alignItems: 'center',
    marginBottom: 6,
  },
  summaryWrap: {
    width: 256,
    minHeight: 70,
    background: '#fff',
    fontSize: 15.5,
    color: '#222',
    margin: '8px 0 0 0',
    lineHeight: 1.5,
    letterSpacing: '-0.2px',
    flex: 1,
    display: 'flex',
    flexDirection: 'column',
    justifyContent: 'flex-start'
  },
  summaryText: {
    marginBottom: 4,
    whiteSpace: 'pre-line',
    wordBreak: 'keep-all'
  },
  bottomBar: {
    width: '100%',
    display: 'flex',
    justifyContent: 'center',
    padding: '18px 0 18px 0',
    background: '#fff',
    borderBottomLeftRadius: 14,
    borderBottomRightRadius: 14,
  },
  voiceButton: {
    display: 'flex',
    alignItems: 'center',
    gap: 8,
    width: 240,
    height: 46,
    background: '#E23A3A',
    color: '#fff',
    fontWeight: 600,
    fontSize: 16,
    borderRadius: 24,
    border: 'none',
    boxShadow: '0 2px 10px 0 rgba(30,30,30,0.09)',
    justifyContent: 'center',
    cursor: 'pointer'
  },
  micIcon: {
    fontSize: 21,
    marginRight: 4,
  },
  voiceButtonText: {
    fontSize: 15.5,
    fontWeight: 600
  }
};
