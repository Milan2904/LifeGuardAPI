from fastapi import FastAPI
from fastapi.responses import JSONResponse


app = FastAPI()


@app.get("/api/v1/user-agreement")
async def get_user_agreement():
    agreement_text = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque dictum neque nisi, "
        "at bibendum purus malesuada nec. Vivamus ac pulvinar sem. Quisque id augue quam. "
        "Aliquam ex nisi, bibendum ut convallis ut, laoreet pellentesque est. Etiam bibendum, "
        "elit vel pretium aliquam, diam tortor ultrices velit, eu vulputate nunc dolor quis erat. "
        "In hac habitasse platea dictumst. Nulla vestibulum lacus non feugiat imperdiet. Donec mi "
        "augue, euismod sed volutpat eu, mollis at lorem. Vestibulum dignissim lacinia tellus "
        "volutpat malesuada. Curabitur augue urna, facilisis non imperdiet at, tempor quis lectus. "
        "Nunc facilisis vestibulum libero commodo varius. Nam interdum tortor eget tincidunt "
        "ullamcorper. Donec tincidunt vel felis a sollicitudin. Sed eu molestie tortor. Donec ac "
        "pulvinar enim, in congue nulla. Etiam tincidunt bibendum tincidunt. Sed eget fermentum "
        "diam. Aliquam consequat laoreet varius. Pellentesque mollis enim sapien, tincidunt ornare "
        "lacus consectetur non. Donec odio magna, mollis nec ligula eget, posuere gravida magna. "
        "Nam ultrices euismod dignissim."
    )

    return JSONResponse(content={
        "agreement": agreement_text,
        "version": "0.0.1",
    })

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=10000)
