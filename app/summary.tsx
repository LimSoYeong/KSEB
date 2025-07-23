import { Ionicons } from '@expo/vector-icons';
import * as Speech from 'expo-speech';
import React, { useState } from 'react';
import { StyleSheet, Text, TouchableOpacity, View } from 'react-native';

export default function SummaryScreen() {
  const [summaryText, setSummaryText] = useState(
    '검사 후 일시적인 붓통, 혈변, 복부 불편감은 정상이며 심한 경우 병원에 연락해야 해요. 식사는 부드러운 음식부터 시작하고, 당일에는 무리한 활동과 장거리 이동을 피해야 해요. 아스피린이나 항혈전제를 복용 중인 경우 출혈 위험이 있으므로 반드시 의사와 상의해야 합니다.'
  );

  const speakText = () => {
    Speech.speak(summaryText, {
      language: 'ko-KR',
      pitch: 1.1,
      rate: 1.0,
    });
  };

  return (
    <View style={styles.container}>
      {/* 상단 뒤로가기 */}
      <View style={styles.header}>
        <Text style={styles.headerText}>다시 찍기</Text>
      </View>

      {/* 이미지 미리보기 자리 */}
      <View style={styles.imagePlaceholder}>
        <Text style={styles.imageText}>사진 미리보기</Text>
      </View>

      {/* 요약 텍스트 */}
      <View style={styles.summaryBox}>
        <Text style={styles.summaryText}>{summaryText}</Text>
      </View>

      {/* 음성 버튼 */}
      <TouchableOpacity style={styles.voiceButton} onPress={speakText}>
        <Ionicons name="mic" size={20} color="white" />
        <Text style={styles.voiceButtonText}>음성으로 전달하기</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#fff', paddingTop: 40 },
  header: {
    paddingHorizontal: 20,
    paddingBottom: 10,
  },
  headerText: {
    fontSize: 16,
    color: '#000',
    fontWeight: 'bold',
  },
  imagePlaceholder: {
    height: 300,
    margin: 20,
    backgroundColor: '#eee',
    borderRadius: 10,
    justifyContent: 'center',
    alignItems: 'center',
  },
  imageText: {
    color: '#aaa',
    fontSize: 16,
  },
  summaryBox: {
    flex: 1,
    marginHorizontal: 20,
  },
  summaryText: {
    fontSize: 16,
    lineHeight: 24,
    color: '#333',
  },
  voiceButton: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#000',
    padding: 15,
    borderRadius: 30,
    margin: 20,
    justifyContent: 'center',
  },
  voiceButtonText: {
    color: '#fff',
    fontSize: 16,
    marginLeft: 10,
  },
});
