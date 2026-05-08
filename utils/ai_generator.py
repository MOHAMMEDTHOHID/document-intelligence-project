import os
from dotenv import load_dotenv

load_dotenv()

class AIGenerator:
    """Generate AI-powered content using templates"""
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        # For demo, we'll use template-based generation
        # In production, integrate with OpenAI/Claude API
    
    def generate_summary(self, text, max_length=300):
        """Generate summary of document"""
        try:
            # Simple extraction-based summary for demo
            sentences = text.split('.')
            
            # Score sentences
            scored_sentences = []
            for sent in sentences[:20]:  # Process first 20 sentences
                if len(sent.split()) > 5:  # Filter short sentences
                    score = self._score_sentence(sent, text)
                    scored_sentences.append((sent.strip(), score))
            
            # Sort by score and get top sentences
            top_sentences = sorted(scored_sentences, key=lambda x: x[1], reverse=True)[:5]
            summary = '. '.join([s[0] for s in top_sentences]) + '.'
            
            return summary
        except Exception as e:
            return f"Error generating summary: {str(e)}"
    
    def generate_notes(self, text):
        """Generate structured notes"""
        try:
            lines = text.split('\n')
            notes = "## Key Notes\n\n"
            
            # Extract important lines (longer sentences)
            for line in lines[:30]:
                if len(line.split()) > 5:
                    notes += f"- {line.strip()}\n"
            
            return notes
        except Exception as e:
            return f"Error generating notes: {str(e)}"
    
    def generate_email(self, text, email_type="summary"):
        """Generate professional email"""
        try:
            summary = self.generate_summary(text, max_length=150)
            
            emails = {
                "summary": f"""Dear Recipient,

Please find below the summary of the document:

{summary}

Best regards,
Document Intelligence Platform""",
                
                "follow-up": f"""Hi,

Following up on our discussion regarding the document:

{summary}

Please let me know if you need any clarification.

Best regards,
Document Intelligence Platform""",
                
                "action_items": f"""Hi Team,

Based on the document review, here are the key points to note:

{summary}

Please take necessary action accordingly.

Best regards,
Document Intelligence Platform"""
            }
            
            return emails.get(email_type.lower(), emails["summary"])
        except Exception as e:
            return f"Error generating email: {str(e)}"
    
    def answer_question(self, text, question):
        """Answer question about document"""
        try:
            # Simple keyword matching for demo
            question_lower = question.lower()
            sentences = text.split('.')
            
            # Find relevant sentences
            relevant = []
            for sent in sentences:
                sent_lower = sent.lower()
                # Check if question keywords are in sentence
                words = question_lower.split()
                if any(word in sent_lower for word in words if len(word) > 3):
                    relevant.append(sent.strip())
            
            if relevant:
                answer = '. '.join(relevant[:3]) + '.'
                return answer
            else:
                return "I could not find a direct answer in the document. Please try a different question."
        except Exception as e:
            return f"Error answering question: {str(e)}"
    
    def _score_sentence(self, sentence, text):
        """Score sentence importance"""
        score = 0
        words = sentence.split()
        
        # Score based on length
        score += len(words) * 0.1
        
        # Score based on word frequency
        for word in words:
            if len(word) > 3:
                count = text.lower().count(word.lower())
                score += count * 0.05
        
        return score
    
    def extract_keywords(self, text, num_keywords=10):
        """Extract important keywords"""
        try:
            words = text.split()
            # Filter stop words
            stop_words = {'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'is', 'was', 'are', 'be', 'been', 'being'}
            
            filtered_words = [w.lower() for w in words if len(w) > 3 and w.lower() not in stop_words]
            
            # Count word frequency
            word_freq = {}
            for word in filtered_words:
                word_freq[word] = word_freq.get(word, 0) + 1
            
            # Get top keywords
            keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:num_keywords]
            
            return [k[0] for k in keywords]
        except Exception as e:
            return []
