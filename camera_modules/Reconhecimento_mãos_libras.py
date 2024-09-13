import cv2
import mediapipe as mp

# Inicializar o MediaPipe para detecção de mãos
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Inicializar a captura de vídeo
cap = cv2.VideoCapture(0)

# Função para reconhecer as vogais com base nas posições dos dedos
def reconhecer_vogal(hand_landmarks):
    thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
    index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
    middle_tip = hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
    ring_tip = hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_TIP]
    pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]

    # Calcular posições y dos dedos em relação ao ponto mais baixo da mão
    thumb_folded = thumb_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_IP].y
    index_folded = index_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_PIP].y
    middle_folded = middle_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.MIDDLE_FINGER_PIP].y
    ring_folded = ring_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.RING_FINGER_PIP].y
    pinky_folded = pinky_tip.y > hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_PIP].y

    # Condições para cada vogal
    if thumb_folded and index_folded and middle_folded and ring_folded and not pinky_folded:
        return "A"
    elif not thumb_folded and index_folded and middle_folded and ring_folded and pinky_folded:
        return "E"
    elif not thumb_folded and not index_folded and middle_folded and ring_folded and pinky_folded:
        return "I"
    elif thumb_folded and not index_folded and not middle_folded and not ring_folded and not pinky_folded:
        return "O"
    elif not thumb_folded and not index_folded and not middle_folded and not ring_folded and not pinky_folded:
        return "U"
    else:
        return None

# Configurações do MediaPipe
with mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=1,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Converte a imagem para RGB (MediaPipe usa RGB ao invés de BGR)
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Flip horizontal para criar um efeito de espelho
        image = cv2.flip(image, 1)

        # Detectar as mãos
        results = hands.process(image)

        # Converter de volta para BGR
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Verificar se alguma mão foi detectada
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                # Desenhar as landmarks da mão na imagem
                mp_drawing.draw_landmarks(
                    image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Reconhecer a vogal com base nas posições dos dedos
                vogal = reconhecer_vogal(hand_landmarks)

                if vogal:
                    cv2.putText(image, f'Vogal: {vogal}', (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)

        # Mostrar a imagem
        cv2.imshow('Webcam', image)

        # Sair do loop ao pressionar 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Liberar recursos
cap.release()
cv2.destroyAllWindows()
