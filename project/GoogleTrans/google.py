import asyncio
from googletrans import Translator

#print(googletrans.LANGUAGES)
async def translate_text(txt):
    t = Translator()
    result = await t.translate(txt, src="vi", dest="ja") 
    return result.text

if __name__ == "__main__":
    asyncio.run(translate_text())