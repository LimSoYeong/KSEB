// src/screens/CameraScreen.tsx

import { Camera } from 'expo-camera';
import { router } from 'expo-router';
import React, { useEffect, useRef, useState } from 'react';
import {
    Dimensions,
    StyleSheet,
    Text,
    TouchableOpacity,
    View,
} from 'react-native';
import {
    PinchGestureHandler,
    PinchGestureHandlerGestureEvent,
} from 'react-native-gesture-handler';
import Animated, {
    useAnimatedGestureHandler,
    useAnimatedProps,
    useSharedValue,
} from 'react-native-reanimated';

const { width } = Dimensions.get('window');
const BUTTON_SIZE = 90;
const OUTER_SIZE = 120;

// AnimatedCamera with zoom animation support
const AnimatedCamera = Animated.createAnimatedComponent(Camera);

export default function CameraScreen() {
  const cameraRef = useRef<Camera>(null);
  const zoom = useSharedValue(0);
  const [permission, requestPermission] = Camera.useCameraPermissions();
  const [isReady, setIsReady] = useState(false);

  useEffect(() => {
    if (permission?.granted) {
      setIsReady(true);
    } else if (permission && !permission.granted) {
      requestPermission();
    }
  }, [permission]);

  const onPinchGestureEvent = useAnimatedGestureHandler<
    PinchGestureHandlerGestureEvent,
    { startZoom: number }
  >({
    onActive: (event) => {
      let newZoom = zoom.value + (event.scale - 1) * 0.05;
      zoom.value = Math.min(Math.max(newZoom, 0), 1); // 0 ~ 1 사이 제한
    },
  });

  const animatedProps = useAnimatedProps(() => ({
    zoom: zoom.value,
  }));

  const takePicture = async () => {
    if (cameraRef.current) {
      try {
        const photo = await cameraRef.current.takePictureAsync();
        console.log('사진 촬영 성공:', photo.uri);
        router.push('/LoadingImage');
      } catch (error) {
        console.error('사진 촬영 실패:', error);
      }
    }
  };

  if (!permission || !permission.granted || !isReady) {
    return (
      <View style={styles.container}>
        <Text style={{ color: '#fff' }}>카메라 권한 요청 중...</Text>
      </View>
    );
  }

  return (
    <View style={styles.container}>
      <PinchGestureHandler onGestureEvent={onPinchGestureEvent}>
        <Animated.View style={{ flex: 1 }}>
          <AnimatedCamera
            ref={cameraRef}
            style={styles.camera}
            ratio="16:9"
            animatedProps={animatedProps}
          >
            <View style={styles.overlay}>
              <Text style={styles.guideText}>읽고 싶은 문서를 찍어주세요</Text>
            </View>
          </AnimatedCamera>
        </Animated.View>
      </PinchGestureHandler>

      <View style={styles.buttonContainer}>
        <View style={styles.outerCircle} />
        <TouchableOpacity style={styles.captureButton} onPress={takePicture} />
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#000' },
  camera: { flex: 1 },
  overlay: {
    position: 'absolute',
    top: 60,
    width: '100%',
    alignItems: 'center',
    zIndex: 10,
  },
  guideText: {
    color: '#fff',
    fontSize: 22,
    fontWeight: 'bold',
    textShadowColor: '#000',
    textShadowOffset: { width: 1, height: 1 },
    textShadowRadius: 4,
  },
  buttonContainer: {
    position: 'absolute',
    bottom: 50,
    width: '100%',
    alignItems: 'center',
    justifyContent: 'center',
    height: OUTER_SIZE,
  },
  outerCircle: {
    position: 'absolute',
    width: OUTER_SIZE,
    height: OUTER_SIZE,
    borderRadius: OUTER_SIZE / 2,
    borderWidth: 5,
    borderColor: '#fff',
    opacity: 0.5,
    bottom: 0,
    alignSelf: 'center',
    zIndex: 1,
  },
  captureButton: {
    width: BUTTON_SIZE,
    height: BUTTON_SIZE,
    borderRadius: BUTTON_SIZE / 2,
    backgroundColor: '#fff',
    borderWidth: 4,
    borderColor: '#eee',
    alignSelf: 'center',
    zIndex: 2,
  },
});
