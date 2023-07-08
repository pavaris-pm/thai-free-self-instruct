# this is for saving the prompt for self-instruct

def get_prompt() -> str:
    prompt = '''
        You are asked to come up with a set of 20 diverse task instructions in Thai language. These task instructions will be given to a GPT model and we will evaluate the GPT model for completing the instructions
Here are the requirements:
1. Try not to repeat the verb for each instruction to maximize diversity.
2. The language used for the instruction also should be diverse. For example, you should combine questions with imperative instructions.
3. The type of instructions should be diverse. The list should include diverse types of tasks like open-ended generation, classification, editing, etc.
4. A GPT language model should be able to complete the instruction. For example, do not ask the assistant to create any visual or audio output. For another example, do not ask the assistant to wake you up at 5pm or set a reminder because it cannot perform any action.
5. The instructions should be in Thai.
6. The instructions should be 1 to 2 sentences long. Either an imperative sentence or a question is permitted.
7. You should generate an appropriate input to the instruction. The input field should contain a specific example provided for the instruction. It should involve realistic data and should not contain simple placeholders. The input should provide substantial content to make the instruction challenging but should ideally not exceed 100 words.
8. Not all instructions require input. For example, when a instruction asks about some general information, "what is the highest peak in the world", it is not necssary to provide a specific context. In this case, we simply put "<noinput>" in the input field.
9. The output should be an appropriate response to the instruction and the input. Make sure the output is less than 100 words.

List of 20 tasks:
###
1. Instruction: ขอกฎหมายที่ควบคุมค่าจ้างขั้นต่ำของรัฐแคลิฟอร์เนีย สหรัฐอเมริกา
1. Input:
<noinput>
1. Output:
ในระดับรัฐบาลกลาง ค่าจ้างขั้นต่ำอยู่ภายใต้พระราชบัญญัติมาตรฐานแรงงานที่เป็นธรรม ปัจจุบันกฎหมายของรัฐบาลกลางกำหนดค่าแรงขั้นต่ำไว้ที่ 7.25 ดอลลาร์ต่อชั่วโมง อย่างไรก็ตาม กฎหมายของรัฐบาลกลางอนุญาตให้รัฐและเมืองต่างๆ กำหนดค่าจ้างขั้นต่ำที่สูงกว่าอัตราของรัฐบาลกลาง 29 USC § 218(ก) รัฐแคลิฟอร์เนียได้กำหนดค่าแรงขั้นต่ำที่สูงกว่าอัตราของรัฐบาลกลาง ดังนั้นนายจ้างในรัฐแคลิฟอร์เนียจึงจำเป็นต้องจ่ายค่าจ้างขั้นต่ำที่กำหนดโดยกฎหมายของรัฐ (เว้นแต่เมืองหรือเคาน์ตีที่ตนดำเนินกิจการอยู่จะมีอัตราที่สูงกว่านั้น) ดู ด้านล่าง รหัสแรงงาน § 1182.12. ค่าจ้างขั้นต่ำของรัฐแคลิฟอร์เนียถูกกำหนดให้ค่อยๆ เพิ่มขึ้นเมื่อเวลาผ่านไป ในปี 2022 ค่าจ้างขั้นต่ำจะอยู่ที่ 14.50 ดอลลาร์ต่อชั่วโมง
###
2. Instruction: ความสัมพันธ์ระหว่างคู่ที่กำหนดคืออะไร?
2. Input:
กลางคืน : วัน :: ขวา : ซ้าย
2. Output:
ความสัมพันธ์ระหว่างคู่ที่กำหนดคือ คู่ตรงข้าม
###
3. Instruction: บุคคลและองค์กรจะลดอคติโดยไม่รู้ตัวได้อย่างไร?
3. Input:
<noinput>
3. Output:
จุดเริ่มต้นที่ดีคือการทำให้ช้าลง การตัดสินใจมักจะได้รับผลกระทบจากอคติโดยไม่รู้ตัวเมื่อทำอย่างรวดเร็วหรืออยู่ภายใต้ความเครียด บางวิธีในการหลีกเลี่ยงการตัดสินอย่างรวดเร็วและป้องกันอคติคือการแสวงหาความคิดเห็นและมุมมองที่แตกต่างกันก่อนที่จะทำการตัดสินใจในการจัดการความสามารถ รับสมัครผู้สมัครจากแหล่งต่างๆ ฝึกอบรมพนักงานข้ามสายงาน สร้างโปรแกรมการให้คำปรึกษาและพันธมิตร และตั้งค่าระบบสำหรับการรายงานโดยไม่เปิดเผยตัวตน ปัญหาและวัดความก้าวหน้า
###
4. Instruction:


    '''

    return prompt
