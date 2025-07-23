import { CameraView, useCameraPermissions } from 'expo-camera';
import * as MediaLibrary from 'expo-media-library';
import React, { useRef, useState } from 'react';
import { Alert, Image, StyleSheet, Text, TouchableOpacity, View } from 'react-native';

export default function CameraScreen() {
  // 카메라 권한 훅
  const [permission, requestPermission] = useCameraPermissions();
  // 앨범 권한
  const [mediaPermission, requestMediaPermission] = MediaLibrary.usePermissions();

  const cameraRef = useRef<CameraView>(null);
  const [photoUri, setPhotoUri] = useState<string | null>(null);

  // 권한 요청 상태 처리
  if (!permission || !mediaPermission) {
    return <View style={styles.center}><Text>카메라 권한 요청 중...</Text></View>;
  }

  if (!permission.granted || !mediaPermission.granted) {
    return (
      <View style={styles.center}>
        <Text>카메라/앨범 접근 권한이 필요합니다.</Text>
        {!permission.granted && (
          <TouchableOpacity style={styles.button} onPress={requestPermission}>
            <Text style={styles.buttonText}>카메라 권한 허용</Text>
          </TouchableOpacity>
        )}
        {!mediaPermission.granted && (
          <TouchableOpacity style={styles.button} onPress={requestMediaPermission}>
            <Text style={styles.buttonText}>앨범 권한 허용</Text>
          </TouchableOpacity>
        )}
      </View>
    );
  }

  // 사진 찍기 함수
  const takePhoto = async () => {
    if (!cameraRef.current) {
      Alert.alert('카메라가 아직 초기화되지 않았습니다.');
      return;
    }

    try {
      const photo = await cameraRef.current.takePictureAsync();
      setPhotoUri(photo.uri);
      try {
        await MediaLibrary.saveToLibraryAsync(photo.uri);
        Alert.alert('✅ 사진이 갤러리에 저장되었습니다!');
      } catch (err) {
        Alert.alert('⚠️ 사진은 찍혔지만 저장되지 않았습니다 (Expo Go에서는 제한)');
        console.warn('MediaLibrary save error:', err);
      }
    } catch (err) {
      Alert.alert('🚫 사진 촬영에 실패했습니다.');
      console.error('Camera capture error:', err);
    }
  };

  return (
    <View style={styles.container}>
      {!photoUri ? (
        <>
          <CameraView
            ref={cameraRef}
            style={styles.camera}
            facing="back"
          />
          <TouchableOpacity style={styles.button} onPress={takePhoto}>
            <Text style={styles.buttonText}>📸 사진 찍기</Text>
          </TouchableOpacity>
        </>
      ) : (
        <>
          <Text style={styles.previewTitle}>📷 사진 미리보기</Text>
          <Image source={{ uri: photoUri }} style={styles.preview} />
          <TouchableOpacity style={styles.button} onPress={() => setPhotoUri(null)}>
            <Text style={styles.buttonText}>↩️ 다시 찍기</Text>
          </TouchableOpacity>
        </>
      )}
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1 },
  center: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  camera: { flex: 1 },
  button: {
    position: 'absolute',
    bottom: 40,
    alignSelf: 'center',
    backgroundColor: '#000',
    padding: 15,
    borderRadius: 10,
    zIndex: 10,
  },
  buttonText: { color: '#fff', fontSize: 18 },
  previewTitle: {
    fontSize: 22,
    textAlign: 'center',
    marginTop: 20,
    fontWeight: 'bold',
  },
  preview: { flex: 1, width: '100%', resizeMode: 'contain' },
});
