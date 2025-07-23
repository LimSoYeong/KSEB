import { router } from 'expo-router';
import { Button, StyleSheet, Text, View } from 'react-native';

export default function RecordPage() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>🎤 음성 질문 녹음 중...</Text>
      <Button title="녹음 종료" onPress={() => router.push('/answer')} />
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center' },
  text: { fontSize: 20, marginBottom: 20 },
});
