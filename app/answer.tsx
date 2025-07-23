import { StyleSheet, Text, View } from 'react-native';

export default function AnswerPage() {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>💬 분석된 답변 결과</Text>
      <Text style={{ marginTop: 20 }}>여기에 음성 분석 결과가 표시될 예정입니다.</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, justifyContent: 'center', alignItems: 'center', padding: 20 },
  text: { fontSize: 20, fontWeight: 'bold' },
});
