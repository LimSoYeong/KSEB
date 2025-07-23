import { Link } from 'expo-router';
import { Button, StyleSheet, Text, View } from 'react-native';

export default function HomeScreen() {
  return (
    <View style={styles.container}>
      <Text style={styles.title}>📱 시선이음 보는 것에서, 이해로. 시선을 잇다. </Text>
      <Link href="/camera" asChild>
        <Button title="Start Camera" />
      </Link>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1, justifyContent: 'center', alignItems: 'center', padding: 20
  },
  title: {
    fontSize: 24, marginBottom: 20
  }
});


// import { StyleSheet, Text, View } from 'react-native';

// export default function HomeScreen() {
//   console.log("✅ index.tsx 렌더링됨");

//   return (
//     <View style={styles.container}>
//       <Text style={styles.title}>✅ 인덱스 렌더링 확인!</Text>
//     </View>
//   );
// }

// const styles = StyleSheet.create({
//   container: {
//     flex: 1, justifyContent: 'center', alignItems: 'center', padding: 20
//   },
//   title: {
//     fontSize: 24, marginBottom: 20
//   }
// });
