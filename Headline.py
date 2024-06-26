from fastapi import FastAPI, Depends, HTTPException, Query, status , Body , Header
from groq import Groq
from Classes import HeadlineRequest
import os

api_key = os.getenv('GROQ_API_KEY')

def headline_check(feild : str = Query(None) , subfeild : str = Query(None) ,  Prev_headline : HeadlineRequest = Body(...) ) -> str :
    if feild and subfeild :
        client = Groq(api_key=f"{api_key}")
        completion = client.chat.completions.create(
            model="mixtral-8x7b-32768",
            messages=[
                {
                    "role": "system",
                    "content": "You are an Expert in Writing Headlines for linkedin profile "
                },
                {
                    "role": "user",
                    "content": f"""The user is  {feild} and expert in {subfeild} . His  headline is ***{Prev_headline}*** . !!!You have to improve this headline in a very professional and apealing way and in refernce to the  headline!!! . Dont give anything more just the improved version of the headline"""
                },
            ],
            temperature=1,
            max_tokens=1024,
            top_p=1,
            stream=False,
            stop=None,
        )

        return(completion.choices[0].message.content)
    else :
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "invalid feild")