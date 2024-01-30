import React, { useState } from 'react';
import { View, TextInput, TouchableOpacity, FlatList, Text, Image, StyleSheet } from 'react-native';

export default function App() {
  const [inputText, setInputText] = useState('');
  const [messages, setMessages] = useState([]);

  const handleSend = async () => {
    try {
      const response = await fetch('http://192.168.1.136:3000/api/chat', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ user_input: inputText }),
      });

      const result = await response.json();

      const newMessage = { text: inputText, sender: 'user' };
      const botMessage = { text: result.response, sender: 'bot' };

      setMessages([...messages, newMessage, botMessage]);
      setInputText('');
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  return (
    <View style={styles.container}>
      <FlatList
        data={messages}
        keyExtractor={(item, index) => index.toString()}
        renderItem={({ item }) => (
          <View style={item.sender === 'user' ? styles.userMessage : styles.botMessage}>
            {item.sender === 'user' && (
              <View style={styles.profileContainer}>
                <Image
                  source={require('./user_profile.png')} // Replace with your user profile picture source
                  style={styles.profileImage}
                />
              </View>
            )}
            <Text>{item.text}</Text>
          </View>
        )}
      />
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.input}
          value={inputText}
          onChangeText={(text) => setInputText(text)}
          placeholder="Type your message..."
        />
        <TouchableOpacity style={styles.sendButton} onPress={handleSend}>
          <Text style={styles.sendButtonText}>Send</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#F5F5F5',
  },
  inputContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    paddingHorizontal: 16,
    paddingVertical: 8,
  },
  input: {
    flex: 1,
    backgroundColor: 'white',
    borderRadius: 20,
    paddingHorizontal: 16,
    marginRight: 8,
  },
  sendButton: {
    backgroundColor: '#4CAF50',
    borderRadius: 20,
    paddingVertical: 10,
    paddingHorizontal: 16,
  },
  sendButtonText: {
    color: 'white',
    fontWeight: 'bold',
  },
  userMessage: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#E0E0E0',
    borderRadius: 10,
    margin: 8,
    padding: 12,
    maxWidth: '70%',
    alignSelf: 'flex-end',
  },
  botMessage: {
    backgroundColor: '#4CAF50',
    borderRadius: 10,
    margin: 8,
    padding: 12,
    maxWidth: '70%',
    alignSelf: 'flex-start',
  },
  profileContainer: {
    position: 'absolute',
    top: 8,
    right: 8,
  },
  profileImage: {
    width: 40,
    height: 40,
    borderRadius: 20,
  },

});
