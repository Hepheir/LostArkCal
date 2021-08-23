from dataclasses import dataclass
from typing import Dict, List, Optional, Union



from requests import Request, Session
from bs4 import BeautifulSoup
from bs4.element import Tag


AUCTION_ITEM_LIST = []

@dataclass
class AuctionItem:
    name: str
    effect: Dict[str, int]
    quality: int
    price_row: int
    price_buy: Optional[int]




def get_auction_data_one_page(page_no: int = 1):
    request_data = {
        "request[firstCategory]": "200000", # 카테고리
        "request[secondCategory]": {
            "목걸이": 200010,
            "귀걸이": 200020,
            "반지": 200030,
        }['목걸이'],

        "request[classNo]": "",
        "request[itemTier]": 3,
        "request[itemGrade]": 5,

        # 아이템 레벨
        "request[itemLevelMin]": 0,
        "request[itemLevelMax]": 1600,


        "request[itemName]": "",
        "request[gradeQuality]": 0,

        # 스킬 상세 옵션
        "request[skillOptionList][0][firstOption]": "",
        "request[skillOptionList][0][secondOption]": "",
        "request[skillOptionList][0][minValue]": "",
        "request[skillOptionList][0][maxValue]": "",

        "request[skillOptionList][1][firstOption]": "",
        "request[skillOptionList][1][secondOption]": "",
        "request[skillOptionList][1][minValue]": "",
        "request[skillOptionList][1][maxValue]": "",

        "request[skillOptionList][2][firstOption]": "",
        "request[skillOptionList][2][secondOption]": "",
        "request[skillOptionList][2][minValue]": "",
        "request[skillOptionList][2][maxValue]": "",

        # 기타 상세 옵션
        "request[etcOptionList][0][firstOption]": 2,
        "request[etcOptionList][0][secondOption]": 15,
        "request[etcOptionList][0][minValue]": "",
        "request[etcOptionList][0][maxValue]": "",

        "request[etcOptionList][1][firstOption]": 2,
        "request[etcOptionList][1][secondOption]": 18,
        "request[etcOptionList][1][minValue]": "",
        "request[etcOptionList][1][maxValue]": "",

        "request[etcOptionList][2][firstOption]": 3,
        "request[etcOptionList][2][secondOption]": "",
        "request[etcOptionList][2][minValue]": "",
        "request[etcOptionList][2][maxValue]": "",

        "request[etcOptionList][3][firstOption]": 3,
        "request[etcOptionList][3][secondOption]": "",
        "request[etcOptionList][3][minValue]": "",
        "request[etcOptionList][3][maxValue]": "",

        "request[pageNo]": page_no,
    }

    session = Session()
    request = Request(
        method='POST',
        url='https://lostark.game.onstove.com/Auction/GetAuctionListV2',
        headers={
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
        },
        data=request_data
    )
    response = session.send(request.prepare())

    auction_item_list: List[AuctionItem]
    auction_item_list = []

    # Parsing

    soup = BeautifulSoup(response.text, 'html.parser')

    tbody: Union[Tag, None]
    tbody = soup.select_one('#auctionListTbody')

    # TODO: 가져온 페이지 별 데이터 파싱
    tbody.text


def main(kwargs):

    # TODO: 여러개의 페이지에서 정보를 최대한 수집

    try:
        for page_no in range(1, 51):


    return response.text


if __name__ == '__main__':
    main(QUERY)
