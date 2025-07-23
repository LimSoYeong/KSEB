// app/loading.tsx
import { router } from 'expo-router';
import { useEffect } from 'react';
import { ActivityIndicator, StyleSheet, Text, View } from 'react-native';

export default function LoadingPage() {
  useEffect(() => {
    const timeout = setTimeout(() => {
      router.push('/summary'); // 문서 분석 끝나면 summary로 이동
    }, 3000); // 3초 대기

    return () => clearTimeout(timeout);
  }, []);

  return (
    <View style={styles.container}>
      <ActivityIndicator size="large" color="#000" />
      <Text style={styles.text}>잠시만 기다려주세요</Text>
      <Text style={styles.subtext}>문서 분석중...</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center', backgroundColor: '#fff' },
  text: { fontSize: 18, fontWeight: 'bold', marginBottom: 10 },
  subtext: { fontSize: 16, color: '#666' },
});
