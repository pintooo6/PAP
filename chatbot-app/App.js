import React from 'react';
import { View, FlatList } from 'react-native';
import ChatBubble from './ChatBubble';
import ChatInput from './ChatInput';

const ChatView = () => {
  const [messages, setMessages] = useState([]);

  const handleSendMessage = (message) => {
    // Send message to the chatbot
    setMessages([...messages, { message, isUserMessage: true }]);
  };

  return (
    <View>
      <FlatList
        data={messages}
        keyExtractor={(message, index) => `message-${index}`}
        renderItem={({ item }) => (
          <ChatBubble message={item.message} isUserMessage={item.isUserMessage} />
        )}
      />
      <ChatInput handleSendMessage={handleSendMessage} />
    </View>
  );
};

export default ChatView;
