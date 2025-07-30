import React, { useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

export default function LoadingPage() {
  const navigate = useNavigate();

  useEffect(() => {
    const timeout = setTimeout(() => {
      navigate('/summary'); // 3초 뒤 summary로 이동
    }, 3000);
    return () => clearTimeout(timeout);
  }, [navigate]);

  return (
    <div style={styles.container}>
      <div style={styles.spinner}></div>
      <div style={styles.text}>잠시만 기다려주세요</div>
      <div style={styles.subtext}>문서 분석중...</div>
    </div>
  );
}

const styles = {
  container: {
    minHeight: '100vh',
    display: 'flex', flexDirection: 'column',
    justifyContent: 'center', alignItems: 'center',
    background: '#fff',
  },
  spinner: {
    width: 48,
    height: 48,
    border: '5px solid #ccc',
    borderTop: '5px solid #333',
    borderRadius: '50%',
    animation: 'spin 1s linear infinite',
    marginBottom: 20,
  },
  text: { fontSize: 18, fontWeight: 'bold', marginBottom: 10 },
  subtext: { fontSize: 16, color: '#666' },
};

// CSS 애니메이션 추가
const styleSheet = document.createElement("style");
styleSheet.innerText = `
@keyframes spin {
  0% { transform: rotate(0deg);}
  100% { transform: rotate(360deg);}
}`;
document.head.appendChild(styleSheet);
