"""
Translate a string
"""
# pylint: disable=import-error
import ctranslate2
import sentencepiece as spm
from app.model.mysql import crud


async def translate_text(params) -> str:
    """
    Translate a string & Save to DB
    """

    mt_text = await ctranslate(params)

    if isinstance(mt_text, str):
        await crud.create_translate(params, mt_text)
        return mt_text


async def ctranslate(params) -> str:
    """
    Translate a string
    - Tokenize using SentencePiece
    - Translate using CTranslate format model
    """
    translator = ctranslate2.Translator(
        f"nmt/model/bin/{params.sl}-{params.tl}", device="cpu")
    # pylint: disable=too-many-function-args
    sp_sl = spm.SentencePieceProcessor(
        f"nmt/model/sentencepiece/sp_model.{params.sl}")
    sp_tl = spm.SentencePieceProcessor(
        f"nmt/model/sentencepiece/sp_model.{params.tl}")

    input_tokens = sp_sl.Encode(params.text, out_type=str)
    results = translator.translate_batch([input_tokens])

    output_tokens = results[0].hypotheses[0]
    output_text = sp_tl.Decode(output_tokens)

    return output_text
