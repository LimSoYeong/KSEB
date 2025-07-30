// import React, { useRef, useState } from 'react';

// function CameraScreen() {
//   const [photo, setPhoto] = useState(null);
//   const videoRef = useRef(null);
//   const canvasRef = useRef(null);

//   // 카메라 켜기
//   const startCamera = async () => {
//     try {
//       const stream = await navigator.mediaDevices.getUserMedia({ video: true });
//       videoRef.current.srcObject = stream;
//     } catch (err) {
//       alert('카메라 권한이 없거나 접근 실패');
//     }
//   };

//   // 사진 촬영
//   const takePhoto = () => {
//     const video = videoRef.current;
//     const canvas = canvasRef.current;
//     const ctx = canvas.getContext('2d');
//     ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
//     canvas.toBlob(blob => {
//       setPhoto(URL.createObjectURL(blob));
//     }, 'image/jpeg');
//   };

//   // 다시 찍기
//   const retakePhoto = () => {
//     setPhoto(null);
//   };

//   return (
//     <div style={{ textAlign: 'center' }}>
//       {!photo ? (
//         <>
//           <video
//             ref={videoRef}
//             autoPlay
//             width="320"
//             height="240"
//             style={{ border: '1px solid #ccc', marginTop: 20 }}
//           />
//           <br />
//           <button onClick={startCamera}>카메라 시작</button>
//           <button onClick={takePhoto}>사진 찍기</button>
//           <canvas ref={canvasRef} width="320" height="240" style={{ display: 'none' }} />
//         </>
//       ) : (
//         <>
//           <h3>사진 미리보기</h3>
//           <img src={photo} alt="캡처" width="320" height="240" style={{ border: '1px solid #ccc' }} />
//           <br />
//           <button onClick={retakePhoto}>↩️ 다시 찍기</button>
//         </>
//       )}
//     </div>
//   );
// }

// export default CameraScreen;

import React, { useRef, useState } from 'react';
import { useNavigate } from 'react-router-dom'; // 추가!

function CameraScreen() {
  const [photo, setPhoto] = useState(null);
  const videoRef = useRef(null);
  const canvasRef = useRef(null);
  const navigate = useNavigate(); // 추가!

  // 카메라 켜기
  const startCamera = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ video: true });
      videoRef.current.srcObject = stream;
    } catch (err) {
      alert('카메라 권한이 없거나 접근 실패');
    }
  };

  // 사진 촬영
  const takePhoto = () => {
    const video = videoRef.current;
    const canvas = canvasRef.current;
    const ctx = canvas.getContext('2d');
    ctx.drawImage(video, 0, 0, canvas.width, canvas.height);
    canvas.toBlob(blob => {
      setPhoto(URL.createObjectURL(blob));
    }, 'image/jpeg');
  };

  // 다시 찍기
  const retakePhoto = () => {
    setPhoto(null);
  };

  // 문서 분석하기
  const goToLoading = () => {
    navigate('/load');
  };

  return (
    <div style={{ textAlign: 'center' }}>
      {!photo ? (
        <>
          <video
            ref={videoRef}
            autoPlay
            width="320"
            height="240"
            style={{ border: '1px solid #ccc', marginTop: 20 }}
          />
          <br />
          <button onClick={startCamera}>카메라 시작</button>
          <button onClick={takePhoto}>사진 찍기</button>
          <canvas ref={canvasRef} width="320" height="240" style={{ display: 'none' }} />
        </>
      ) : (
        <>
          <h3>사진 미리보기</h3>
          <img src={photo} alt="캡처" width="320" height="240" style={{ border: '1px solid #ccc' }} />
          <br />
          <button onClick={retakePhoto}>↩️ 다시 찍기</button>
          {/* 문서 분석하기 버튼 */}
          <button onClick={goToLoading} style={{ marginLeft: 10 }}>문서 분석하기</button>
        </>
      )}
    </div>
  );
}

export default CameraScreen;

