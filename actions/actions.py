# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

import psycopg2
import csv

# Update connection string information
# host = "rasapostresql.postgres.database.azure.com"
# dbname = "userinfo"
# user = "rasaptsql@rasapostresql"
# password = "Password012"
# sslmode = "require"

# This is a simple example for a custom action which utters "Hello World!"
# class ActionHelloWorld(Action):

#     def name(self) -> Text:
#         return "action_hello_world"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         dispatcher.utter_message(text="Hello World!")

#         return []

class ActionUtterMetrostarLocation(Action):

    def name(self) -> Text:
        return "action_utter_metrostar_location"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # dispatcher.utter_message(
        #     text=(
        #         "VỊ TRÍ CHIẾN LƯỢC"
        #         "\n-Metro Star tọa lạc tại 360 Xa Lộ Hà Nội, TP. Thủ Đức - đoạn đẹp nhất trên cung đường Xa Lộ Hà Nội."
        #         "\n-Metro Star là dự án duy nhất có cầu vượt bộ hành nối thẳng từ tầng 2 của Dự án (Khu Trung tâm thương mại) băng ngang qua XLHN để đi vào trạm số 10 Metro, chỉ 10 phút sau bạn đã có mặt ở trung tâm Quận 1."
        #         "\n=> Nhờ nằm ở phía đối diện ga metro với bãi cỏ rộng mênh mông và công viên thoáng đãng phía trước, khu căn hộ tránh được tiếng ồn từ ga metro cũng như XLHN - điều mà các dự án nằm cùng phía với đường tàu không thể có được. Và cũng không có nơi nào lợi nhuận tương lai nhiều hơn bất động sản ngay tại Ga Metro..."
        #         "\nĐịa chỉ: 360 Xa Lộ Hà Nội, TP. Thủ Đức, TP.HCM."
        #     ),
        #     buttons=[
        #         {"title": "Tìm hiểu nội khu", "payload": "Nội khu thế nào"},
        #         {"title": "Chính sách bán hàng", "payload": "Chính sách bán hàng"},
        #         {"title": "Tiến độ dự án", "payload": "Tiến độ dự án"}
        #     ]
        # )
        dispatcher.utter_message(text="VỊ TRÍ CHIẾN LƯỢC")
        dispatcher.utter_message(text="-Metro Star tọa lạc tại 360 Xa Lộ Hà Nội, TP. Thủ Đức - đoạn đẹp nhất trên cung đường Xa Lộ Hà Nội.")
        dispatcher.utter_message(text="-Metro Star là dự án duy nhất có cầu vượt bộ hành nối thẳng từ tầng 2 của Dự án (Khu Trung tâm thương mại) băng ngang qua XLHN để đi vào trạm số 10 Metro, chỉ 10 phút sau bạn đã có mặt ở trung tâm Quận 1.")
        dispatcher.utter_message(text="=> Nhờ nằm ở phía đối diện ga metro với bãi cỏ rộng mênh mông và công viên thoáng đãng phía trước, khu căn hộ tránh được tiếng ồn từ ga metro cũng như XLHN - điều mà các dự án nằm cùng phía với đường tàu không thể có được. Và cũng không có nơi nào lợi nhuận tương lai nhiều hơn bất động sản ngay tại Ga Metro...")
        dispatcher.utter_message(
            text="Địa chỉ: 360 Xa Lộ Hà Nội, TP. Thủ Đức, TP.HCM.",
            buttons=[
                {"title": "Tìm hiểu nội khu", "payload": "Nội khu thế nào"},
                {"title": "Chính sách bán hàng", "payload": "Chính sách bán hàng"},
                {"title": "Tiến độ dự án", "payload": "Tiến độ dự án"}
            ]
        )

        return []

class ActionUtterLoanProcedure(Action):

    def name(self) -> Text:
        return "action_utter_loan_procedure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        # dispatcher.utter_message(
        #     text=(
        #         "Danh mục hồ sơ vay vốn dự kiến bao gồm:"
        #         "\n(1) Hợp đồng mua bán căn hộ (bản gốc)"
        #         "\n(2) Giấy CMND và hộ khẩu của vợ chồng, đăng ký kết hôn/ xác nhận độc thân (sao y công chứng)"
        #         "\n(3) Giấy đề nghị vay vốn kèm phương án trả nợ"
        #         "\n(4) Hồ sơ chứng minh thu nhập đủ để trả nợ, bao gồm:"
        #         "\na) Thu nhập từ lương: Hợp đồng lao động; Sao kê tài lương 3 tháng gần nhất"
        #         "\nb) Thu nhập từ cho thuê nhà đất, căn hộ, xe ô tô: Sổ hồng nhà đất/Hợp đồng mua bán nhà/Cavet xe ô tô đứng tên người vay; Hợp đồng cho thuê"
        #         "\nc) Thu nhập từ hoạt động kinh doanh Công ty: Giấy phép kinh doanh, Điều lệ công ty; Báo cáo tài chính 3 năm gần nhất; Tờ khai VAT (12 tháng gần nhất); Hợp đồng mua bán và hóa đơn VAT có giá trị cao."
        #         "\n(5) Các giấy tờ khác theo yêu cầu của ngân hàng."
        #     ),
        #     buttons=[
        #         {"title": "Tư vấn ngay", "payload": "Tôi cần tư vấn thêm"},
        #         {"title": "Chế độ vay", "payload": "Chế độ vay"},
        #         {"title": "Lãi suất vay ưu đãi", "payload": "Lãi suất vay ưu đãi"}
        #     ]
        # )
        dispatcher.utter_message(text="Danh mục hồ sơ vay vốn dự kiến bao gồm:")
        dispatcher.utter_message(text="(1) Hợp đồng mua bán căn hộ (bản gốc)")
        dispatcher.utter_message(text="(2) Giấy CMND và hộ khẩu của vợ chồng, đăng ký kết hôn/ xác nhận độc thân (sao y công chứng)")
        dispatcher.utter_message(text="(3) Giấy đề nghị vay vốn kèm phương án trả nợ")
        dispatcher.utter_message(text="(4) Hồ sơ chứng minh thu nhập đủ để trả nợ, bao gồm:")
        dispatcher.utter_message(text="a) Thu nhập từ lương: Hợp đồng lao động; Sao kê tài lương 3 tháng gần nhất")
        dispatcher.utter_message(text="b) Thu nhập từ cho thuê nhà đất, căn hộ, xe ô tô: Sổ hồng nhà đất/Hợp đồng mua bán nhà/Cavet xe ô tô đứng tên người vay; Hợp đồng cho thuê")
        dispatcher.utter_message(text="c) Thu nhập từ hoạt động kinh doanh Công ty: Giấy phép kinh doanh, Điều lệ công ty; Báo cáo tài chính 3 năm gần nhất; Tờ khai VAT (12 tháng gần nhất); Hợp đồng mua bán và hóa đơn VAT có giá trị cao.")
        dispatcher.utter_message(
            text="(5) Các giấy tờ khác theo yêu cầu của ngân hàng.",
            buttons=[
                {"title": "Tư vấn ngay", "payload": "Tôi cần tư vấn thêm"},
                {"title": "Chế độ vay", "payload": "Chế độ vay"},
                {"title": "Lãi suất vay ưu đãi", "payload": "Lãi suất vay ưu đãi"}
            ]
        )

        return []

class ActionUtterHowToPay(Action):

    def name(self) -> Text:
        return "action_utter_how_to_pay"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Khách hàng lựa chọn hình thức Chuyển khoản hoặc đóng tiền mặt theo lịch trình thanh toán quy định tại Phụ Lục 02 Hợp đồng mua bán")
        dispatcher.utter_message(
            text=(
                "Thông tin tài khoản ngân hàng và cú pháp chuyển khoản như sau:"
                "\nNgân hàng TMCP Quân Đội:"
                "\nOr Military Commercial Joint Stock Bank:"
                "\n- Đơn vị hưởng /Recipient : CÔNG TY TNHH ĐẦU TƯ METRO STAR"
                "\n- Số tài khoản/ Bank accountant number: 747 117 298 93 82"
                "\n- Tại Ngân hàng/ At the Bank: TMCP QUÂN ĐỘI - SỞ GIAO DỊCH 2"
                "\n- Swift code: MSCBVNVX"
                "\n*Cú pháp chuyển khoản: Tên KH_TT tien mua can ho (mã CH)_du an Metro Star*"
                "\nVí dụ: Nguyễn Văn A - TT tiền mua căn hộ T1-B16-05 _Dự án Metro Star"
            )
        )
        dispatcher.utter_message(text="Việc thanh toán nhà hình thành trong tương lai sẽ thực hiện theo quy định của pháp luật, CĐT sẽ áp dụng phù hợp với các quy định này. Đối với dự án Metro Star, việc thanh toán sẽ được quy định chi tiết tại Hợp Đồng này.")
        dispatcher.utter_message(text="Tiến độ thanh toán chi tiết được quy định tại Hợp đồng mua bán. Hiện tại, chưa có chương trình ưu đãi cho KH thanh toán vượt tiến độ.")
        dispatcher.utter_message(
            text="Nếu chậm thanh toán. Tùy từng trường hợp, Chủ đầu tư có thể xem xét chấp thuận cho gia hạn thêm một thời hạn nhất định.",
            buttons=[
                {"title": "Số tiền cần thanh toán", "payload": "Số tiền cần thanh toán"},
                {"title": "Tư vấn ngay", "payload": "Tư vấn cho tôi"}
            ]
        )

        return []

class ActionUtterAmountOfMoneyToPay(Action):

    def name(self) -> Text:
        return "action_utter_amount_of_money_to_pay"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Số tiền cần thanh toán:")
        dispatcher.utter_message(
            text=(
                "-Khi nhận được mail của Khách hàng liên hệ để hỏi về số tiền cần thanh toán, forward email đó đến địa chỉ: phongketoan@metrostar.vn và cc đến email của khách hàng. Luu ý: Thông tin WS cho phòng KT để phản hồi kịp thời cho khách"
                "\nNội dung email như sau:"
                "\nKính gửi phòng kế toán,"
                "\nNhờ phòng kế toán kiểm tra và thông báo đến khách hàng số tiền cần thanh toán."
            )
        )
        dispatcher.utter_message(
            text=(
                "-Khi nhận được mail của Khách hàng liên hệ cần xác nhận thanh toán thành công, forward email đó đến địa chỉ: phongketoan@metrostar.vn và cc đến email của khách hàng."
                "\nNội dung email như sau:"
                "\nKính gửi phòng kế toán,"
                "\nNhờ phòng kế toán kiểm tra và thông báo đến khách hàng."
                "\nTrân trọng và cảm ơn."
            )
        )
        dispatcher.utter_message(
            text="-Trong trường hợp khách liên hệ hotline hoặc gặp trực tiếp, cần thông tin tới P.KT để nhận thông tin cung cấp cho khách hàng",
            buttons=[
                {"title": "Cách thanh toán", "payload": "Thanh toán như thế nào"},
                {"title": "Tư vấn ngay", "payload": "Tư vấn cho tôi"}
            ]
        )
        
        return []

class ActionUtterUtilityDetail(Action):

    def name(self) -> Text:
        return "action_utter_utility_detail"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="100+ SAO TIỆN ÍCH")
        dispatcher.utter_message(text="Metro Star kết nối 100+ sao tiện ích hoàn hảo phục vụ mọi nhu cầu cuộc sống của những cư dân thành thị hiện đại từ mua sắm, thư giãn, ăn uống, vui chơi giải trí... Một môi trường sống thân thiện với thiên nhiên và thỏa mãn nhu cầu của mọi cư dân dù là độ tuổi nào.")
        dispatcher.utter_message(
            text="Sinh sống tại Metro Star, cư dân được tận hưởng tiện ích nội khu đa dạng như 7 kỳ quan Singapore, Cầu vượt vào ga Metro, Sky Bridge ngắm sông Sài Gòn, nhiều Hồ bơi và Jacuzzi, khu ăn uống ngoài trời, vườn trồng rau, khu mua sắm, hệ thống quản lý thông minh... Bên cạnh đó là các tiện ích ngoại khu đắt giá dọc Xa lộ Hà Nội như Trung tâm thương mại, bệnh viện, trường học Quốc tế, tổ hợp giải trí - thể thao Rạch Chiếc...",
            buttons=[
                {"title": "Tư vấn ngay", "payload": "Tư vấn cho mình"}
            ]
        )
        
        return []

class ActionUtterLegalDocs(Action):

    def name(self) -> Text:
        return "action_utter_legal_docs"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Dự án Metro Star có đầy đủ pháp lý:")
        dispatcher.utter_message(text="(1) Quyết định phê duyệt dự án đầu tư xây dựng số 73/QD-SXD-PTN [Quyết định đã phê duyệt rõ Dự Án không phải Giấy phép xây dựng theo Nghị định 90/2006/NĐ-CP]")
        dispatcher.utter_message(text="(2) Giấy chứng nhận quyền sử dụng đất số CV634124 cấp ngày 15/06/2020")
        dispatcher.utter_message(text="(3) Dự án được UBND TP Chấp thuận chuyển nhượng dự án tại Quyết định số 5268/QĐ-UBND ngày 07/10/2016 xác nhận xong món, hầm.")
        dispatcher.utter_message(text="(4) Quyết định phê duyệt và điều chỉnh cục bộ 1/2000 số 5147/QĐ-UBND cấp ngày 19/11/2018")
        dispatcher.utter_message(text="(5) Quyết định phê duyệt Quy hoạch chi tiết tỷ lệ 1/500 => Dự án có quy mô dưới 02ha, nên không thực hiện thủ tục phê duyệt Quy hoạch chi tiết tỷ lệ 1/500 theo quy định pháp luật hiện hành.")
        dispatcher.utter_message(text="(6) Thẩm duyệt PCCC số 1325/TD-PCCC ngày 31/10/2019")
        dispatcher.utter_message(text="(7) Dự án đã được UBND TP Phê duyệt kế hoạch phát triển nhà ở tại Quyết định số 1757/QĐ-UBND ngày 08/05/2019.")
        dispatcher.utter_message(text="(8) Biên bản nghiệm thu hoàn thành hạng mục phần móng cọc.")
        dispatcher.utter_message(text="(9) Tờ trình đề xuất số 17/TTr-HĐTĐCNDA ngày 16/09/2016 báo cáo UBND Thành phố trước khi UBND Thành phố ký ban hành quyết định số 5268/QĐ-UBND cho phép chuyển nhượng dự án.")
        dispatcher.utter_message(text="(10) Văn bản báo cáo tình hình thi công tại dự án của Apave ký ngày 23/10/2020 (Apave là Công ty Giám sát nổi tiếng của Cộng hòa Pháp thành lập từ năm 1867)")
        dispatcher.utter_message(text="(11) Văn bản số 7234/TB-SCT ngày 24/12/2020 v/v Chấp thuận hồ sơ đăng ký HĐ theo mẫu.")
        dispatcher.utter_message(text="-Dự án Metro Star đủ điều kiện, và ký HĐMB trước khi chuyển nhượng, có xác nhận của UBND TP.HCM việc hoàn thành móng và ký HĐMB tại Quyết định số 5268/QĐ-UBND.")
        dispatcher.utter_message(text="-Xin giải thích chuyên môn về việc chuyển nhượng dự án theo Nghị định 76 - do Sở Xây dựng Chủ trì.")
        dispatcher.utter_message(text="+ Thứ nhất, Sở Xây dựng là đơn vị chủ trì thực hiện Nghị định 76.")
        dispatcher.utter_message(text="+ Thứ hai, để có Quyết định số 5268/QĐ-UBND ngày 07/10/2016 của UBND TP.HCM về việc chấp thuận cho chuyển nhượng Dự án theo Nghị định 76 thì phải thỏa mãn các Quy định:")
        dispatcher.utter_message(text="* Hoàn thành nghĩa vụ tài chính, phải có Sổ đỏ, Giấy phép xây dựng hoặc quyết định tương đương, có Sở Xây dựng kiểm tra và xác nhận dự án đã  xây dựng xong phần móng, đăng báo 3 kỳ liên tiếp thông báo trên phương tiện thông tin đại chúng trước 15 ngày và không có ai khiếu nại.")
        dispatcher.utter_message(text="* Sở Xây dựng đã kiểm tra hồ sơ nghiệm thu hoàn thành phần móng cũng như hiện trạng công trình (dự án đã đủ điều kiện và đang mở bán trước  khi chuyển nhượng).")
        dispatcher.utter_message(
            text="* Ngoài ra, Sở Xây dựng cũng đã lấy ý kiến của các sở ngành liên quan như Sở Kế hoạch và Đầu tư, Sở Tài chính, Sở Tài Nguyên và Môi trường, Cục thuế... Tổ chức thẩm định theo quy định tại điều 14 của Nghị định 76/2015/NĐ-CP và đã có Tờ trình đề xuất số 17/TTr-HĐTĐCNDA ngày 16/09/2016  báo cáo UBND Thành phố trước khi UBND Thành phố ký ban hành quyết định số 5268/QĐ-UBND cho phép chuyển nhượng dự án.",
            buttons=[
                {"title": "Công văn huy động vốn", "payload": "Công văn huy động vốn"},
                {"title": "Giấy phép xây dựng", "payload": "Giấy phép xây dựng"},
                {"title": "Giấy phép xây dựng 30 tầng", "payload": "Giấy phép xây dựng 30 tầng"}
            ]
        )

        return []

class ActionUtterRaiseCapitalLetter(Action):

    def name(self) -> Text:
        return "action_utter_raise_capital_letter"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Công văn huy động vốn")
        dispatcher.utter_message(text="- Dự án Khu chung cư và thương mại Metro Star được Ủy ban nhân dân Thành phố Chấp thuận cho chuyển nhượng dự án từ Công ty Công ty CP Giao thông Công chánh (là Công ty tư nhân và hoạt động theo luật doanh nghiệp, việc chuyển nhượng tài sản của công ty cổ phần thuộc thẩm quyền của Hội đồng quản trị của công ty) sang Công ty TNHH Đầu tư Metro Star (tên cũ là Công ty TNHH Ngôi nhà thân yêu I-Home) tại Quyết định số 5268/QĐ-UBND ngày 07/10/2016 theo Nghị định 76/2015/NĐ-CP ngày 10/09/2015.")
        dispatcher.utter_message(text="- Để được chấp thuận cho chuyển nhượng Dự án theo Nghị định 76 thì phải thỏa mãn các Quy định: Hoàn thành nghĩa vụ tài chính, phải có Sổ đỏ, Giấy phép xây dựng hoặc quyết định tương đương, có Sở Xây dựng kiểm tra và xác nhận dự án đã  xây dựng xong phần móng, đăng báo 3 kỳ kiên tiếp thông báo trên phương tiện thông tin đại chúng trước 15 ngày và không có ai khiếu nại. Sở Xây dựng đã kiểm tra hồ sơ nghiệm thu hoàn thành phần móng cũng như hiện trạng công trình (dự án đã đủ điều kiện và mở bán trước khi chuyển nhượng).")
        dispatcher.utter_message(text="- Ngoài ra, Sở Xây dựng cũng đã lấy ý kiến của các sở ngành liên quan như Sở Kế hoạch và Đầu tư, Sở Tài chính, Sở Tài Nguyên và Môi trường, Cục thuế... Tổ chức thẩm định theo quy định tại điều 14 của Nghị định 76/2015/NĐ-CP và đã có Tờ trình đề xuất số 17/TTr-HĐTĐCNDA ngày 16/09/2016  báo cáo UBND Thành phố trước khi UBND Thành phố ký ban hành quyết định số 5268/QĐ-UBND cho phép chuyển nhượng dự án.")
        dispatcher.utter_message(
            text="- Xin nói thêm là việc chuyển nhượng Dự án theo Nghị định 76 là cực kỳ khó khăn, kéo dài  nên trên thị trường chỉ có khoảng 1% dự án là được chuyển nhượng theo hình thức này, còn lại theo hình thức chuyển nhượng cổ phần công ty.",
            buttons=[
                {"title": "Pháp lý của dự án", "payload": "Pháp lý của dự án"},
                {"title": "Giấy phép xây dựng", "payload": "Giấy phép xây dựng"},
                {"title": "Giấy phép xây dựng 30 tầng", "payload": "Giấy phép xây dựng 30 tầng"}
            ]
        )

        return []

class ActionUtter30FloorsConstructionPermit(Action):

    def name(self) -> Text:
        return "action_utter_30_floors_construction_permit"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Giấy phép xây dựng 30 tầng:")
        dispatcher.utter_message(text="- Dự án được phê duyệt theo Quyết định 73/QĐ-SXD-PTN, theo điều 2. Quyền và nghĩa vụ của CĐT: Thực hiện theo điều 15 Nghị Định 90/2006/NĐ-CP ngày 06/09/2006 của Chính phủ và không phải xin phép xây dựng đối với  công trình trong phạm vi dự án được Phê duyệt tại Quyết định này...")
        dispatcher.utter_message(text="- Dự án được UBND TP Chấp thuận chuyển nhượng dự án tại Quyết định số 5268/QĐ-UBND ngày 07/10/2016 xác nhận xong món, hầm.")
        dispatcher.utter_message(text="- Dự án đã được Ủy ban nhân dân Thành phố có Quyết định 5147/QĐ-UBND ngày 19/11/2018 duyệt điều chỉnh quy mô dự án lên 30 tầng, hệ số sử dụng đất 7,2...")
        dispatcher.utter_message(text="- Dự án được Sở QHKT có văn bản cung cấp chỉ tiêu QHKT chi tiết khu đất tại VB 2709/SQHKT-QHKTT ngày 11/06/2019.")
        dispatcher.utter_message(
            text="- Dự án đã được UBND Thành phố cập nhật kế hoạch phát triển nhà ở tại văn bản 1757/QĐ-UBND ngày 08/05/2020. Phụ lục Quận 9, STT 12 thể hiện rõ tên và quy mô dự án.",
            buttons=[
                {"title": "Pháp lý của dự án", "payload": "Pháp lý của dự án"},
                {"title": "Giấy phép xây dựng", "payload": "Giấy phép xây dựng"},
                {"title": "Công văn huy động vốn", "payload": "Công văn huy động vốn"}
            ]
        )

        return []

class ActionUtterSaleContractSignningCondition(Action):

    def name(self) -> Text:
        return "action_utter_sale_contract_signning_condition"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Điều kiện để được phép ký HĐMB với KH theo quy định gồm có:")
        dispatcher.utter_message(text="(1) Có giấy tờ về quyền sử dụng đất.")
        dispatcher.utter_message(text="(2) Đã hoàn thành móng cọc và nghiệm thu.")
        dispatcher.utter_message(text="(3) Có văn bản thông báo đến Sở xây dựng về việc bán hàng (người khác hay gọi là công văn huy động vốn).")
        dispatcher.utter_message(text="Thực tế Dự Án: Đã đáp ứng đầy đủ và hồ sơ pháp lý đã đầy đủ như sau:")
        dispatcher.utter_message(text="[1] Đã có Giấy chứng nhận quyền sử dụng đất đối với Dự án.")
        dispatcher.utter_message(text="- Tên chủ đầu tư: Công ty TNHH Đầu tư Metro Star")
        dispatcher.utter_message(text="(tên cũ trước đó là Công ty TNHH Ngôi Nhà Thân Yêu I - Home đã được đổi theo quy định luật doanh nghiệp). Xem Giấy phép doanh nghiệp đính kèm.")
        dispatcher.utter_message(text="- Mục đích sử dụng đất: Đất ở Khu dân cư")
        dispatcher.utter_message(text="- Thời hạn sử dụng đất: Lâu dài")
        dispatcher.utter_message(text="[2] Văn bản số 7234/TB-SCT ngày 24/12/2020 v/v Chấp thuận hồ sơ đăng ký HĐ theo mẫu.")
        dispatcher.utter_message(text="[3] Để được chấp thuận cho chuyển nhượng Dự án theo Nghị định 76 thì phải thỏa mãn các Quy định:")
        dispatcher.utter_message(text="- Hoàn thành nghĩa vụ tài chính, phải có Sổ đỏ, Giấy phép xây dựng hoặc quyết định tương đương, có Sở Xây dựng kiểm tra và xác nhận dự án đã xây dựng xong phần móng, đăng báo 3 kỳ kiên tiếp thông báo trên phương tiện thông tin đại chúng trước 15 ngày và không có ai khiếu nại.")
        dispatcher.utter_message(text="- Sở Xây dựng đã kiểm tra hồ sơ nghiệm thu hoàn thành phần móng cũng như hiện trạng công trình (dự án đã đủ điều kiện và mở bán trước khi chuyển nhượng).")
        dispatcher.utter_message(text="- Ngoài ra, Sở Xây dựng cũng đã lấy ý kiến của các sở ngành liên quan như Sở Kế hoạch và Đầu tư, Sở Tài chính, Sở Tài Nguyên và Môi trường, Cục thuế… Tổ chức thẩm định theo quy định tại điều 14 của Nghị định 76/2015/NĐ-CP và đã có Tờ trình đề xuất số 17/TTr-HĐTĐCNDA ngày 16/09/2016 báo cáo UBND Thành phố trước khi UBND Thành phố ký ban hành quyết định số 5268/QĐ-UBND cho phép chuyển nhượng dự án.")
        dispatcher.utter_message(text="Dự án đã hoàn thành móng cọc, được cơ quan chức năng kiểm tra và kết luận về điều kiện ký Hợp đồng căn cứ vào mục 1.2 Quyết dịnh 5268/QĐ-UBND.")
        dispatcher.utter_message(
            text="Mẫu HĐMB đã được Sở công Thương phê duyệt theo văn bản số 7234/TB-SCT ngày 24/12/2020 v/v Chấp thuận hồ sơ đăng ký HĐ theo mẫu",
            buttons=[
                {"title": "Tư vấn ngay", "payload": "Tôi cần tư vấn ngay"}
            ]
        )

        return []

class ActionUtterBankGuarantee(Action):

    def name(self) -> Text:
        return "action_utter_bank_guarantee"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(
            text=(
                "-Đã có các ngân hàng sẵn sàng bảo lãnh"
                "\n-Việc bảo lãnh bàn giao thực hiện theo thỏa thuận của hai bên."
                "\n-Nếu Khách hàng muốn CĐT mở bảo lãnh bàn giao thì đóng thêm 1 khoản phí để thực hiện việc này."
                "\n-Mức phí theo quy định của ngân hàng."
            )
            
        )
        dispatcher.utter_message(text="Việc mở thư bảo lãnh là phải trả phí cho ngân hàng, thường sẽ tính vào giá bán. Tuy nhiên, theo thỏa thuận với khách hàng đã ký thì chúng tôi đã không tính vào giá bán nên nếu Khách hàng muốn mở thì chuyển thanh toán bổ sung phí cho chúng tôi để chúng tôi thanh toán cho ngân hàng.")
        dispatcher.utter_message(
            text=(
                "-Ngân hàng MB, NAB mở bảo lãnh hoặc ngân hàng khác hoạt động hợp pháp tại Việt Nam."
                "\n-Việc mở bảo lãnh hay không tùy khách hàng chọn."
            ),
            buttons=[
                {"title": "Tư vấn thêm", "payload": "Tôi cần tư vấn thêm"}
            ]
        )

        return []

class ActionUtterSaleContractSignningTime(Action):

    def name(self) -> Text:
        return "action_utter_sale_contract_signning_time"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Thời gian ký kết:")
        dispatcher.utter_message(text="- Theo quy định của công ty, khách hàng có tối đa 08 ngày làm việc kể từ ngày ký đặt cọc thành công. Tuy nhiên, trong trường hợp Quý khách hàng có nhu cầu tiếp tục hợp đồng nhưng chưa thể thanh toán trong thời gian này thì Khách hàng vui lòng liên hệ Phòng Dịch vụ khách hàng (P.DVKH) để trao đổi và đưa ra ngày dự kiến thanh toán để P.DVKH có cơ sở trình Ban lãnh đạo.")
        dispatcher.utter_message(text="- Hình thức liên hệ là gặp trực tiếp P. DVKH tại văn phòng Số 117 Nguyễn Đình Chiểu, Phường 06, Quận 03, Thành Phố Hồ Chí Minh (Tầng 02, Tòa nhà Léman Luxury Office).")
        dispatcher.utter_message(
            text="Khi đến địa chỉ trên, Quý khách vui lòng mang theo tất cả giấy tờ liên quan đến dự án Metro Star và giấy tờ tùy thân (CMND và Hộ khẩu)",
            buttons=[
                {"title": "Thủ tục ký kết", "payload": "Thủ tục ký kết hợp đồng mua bán"},
                {"title": "Hồ sơ ký kết", "payload": "Hồ sơ ký kết hợp đồng mua bán"},
                {"title": "Thay đổi thông tin hợp đồng", "payload": "Thay đổi thông tin hợp đồng mua bán"}
            ]
        )

        return []

class ActionUtterSaleContractTranferFile(Action):

    def name(self) -> Text:
        return "action_utter_sale_contract_transfer_file"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="DANH MỤC HỒ SƠ KHÁCH HÀNG CẦN CUNG CẤP KHI CHUYỂN NHƯỢNG HĐMB")
        dispatcher.utter_message(text="(1) Đối với khách hàng chuyển nhượng")
        dispatcher.utter_message(text="- CMND, hộ khẩu của khách hàng đang đứng tên trên HĐ")
        dispatcher.utter_message(text="- Trong trường hợp đã kết hôn cung cấp thêm: CMND, hộ khẩu của vợ/chồng, Giấy chứng nhận đăng ký kết hôn")
        dispatcher.utter_message(text="- Trong trường hợp độc thân: Giấy xác nhận độc thân")
        dispatcher.utter_message(text="- Phiếu đề nghị giữ chỗ không hoàn lại/TTKKHĐMB")
        dispatcher.utter_message(text="- Xác nhận thanh toán đợt 1 (15% GTHĐ)")
        dispatcher.utter_message(text="(2) Đối với khách hàng nhận chuyển nhượng: CMND, hộ khẩu")
        dispatcher.utter_message(text="+ Lưu ý: Tất cả các hồ sơ trên đều được sao y, công chứng trong vòng 06 tháng")
        dispatcher.utter_message(text="(3) Hồ sơ chuyển nhượng cần chuẩn bị:")
        dispatcher.utter_message(text="- Đơn đề nghị chuyển nhượng")
        dispatcher.utter_message(text="- Văn bản cam kết liêm chính")
        dispatcher.utter_message(
            text="- Phiếu tiếp nhận thông tin KH ký kết HĐ/chuyển nhượng HĐ",
            buttons=[
                {"title": "Thủ tục chuyển nhượng", "payload": "Thủ tục chuyển nhượng hợp đồng mua bán"},
                {"title": "Phí chuyển nhượng", "payload": "Phí chuyển nhượng hợp đồng mua bán"},
                {"title": "Tư vấn thêm", "payload": "Tư vấn thêm"}
            ]
        )

        return []

class ActionUtterSaleContractTransferProcedure(Action):

    def name(self) -> Text:
        return "action_utter_sale_contract_transfer_procedure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="-Khi có nhu cầu chuyển nhượng, đầu tiên Bên Mua thông báo bằng văn bản đến Sàn giao dịch bất động sản của Bên Bán theo thông tin như dưới đây và Bên Bán là bên đầu tiên phải đảm bảo xem xét mua Căn Hộ, trường hợp không mua lại Căn Hộ thì Bên Bán thông báo cho Bên Mua trong vòng 07 (bảy) ngày làm việc và hỗ trợ tìm kiếm Khách hàng tốt cho Bên Mua.")
        dispatcher.utter_message(text="-Sàn giao dịch bất động sản chuyên trách việc chuyển nhượng, gọi tắt là Sàn Chuyển Nhượng theo địa chỉ tại số 360 Xa Lộ Hà Nội, Phường Phước Long A, Quận 9, TP.HCM hoặc email: chuyennhuong@metrostar.vn hoặc viber qua số điện thoại: (090 789 6565).")
        dispatcher.utter_message(
            text="-Trường hợp bên chuyển nhượng không thực hiện theo quy trình nêu trên thì Bên Bán có quyền từ chối không hỗ trợ thủ tục chuyển nhượng.",
            buttons=[
                {"title": "Hồ sơ chuyển nhượng", "payload": "Hồ sơ chuyển nhượng hợp đồng mua bán"},
                {"title": "Phí chuyển nhượng", "payload": "Phí chuyển nhượng hợp đồng mua bán"}
            ]
        )

        return []

class ActionUtterLiquidationProcedure(Action):

    def name(self) -> Text:
        return "action_utter_liquidation_procedure"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        dispatcher.utter_message(text="Khách hàng muốn thanh lý thì cần:")
        dispatcher.utter_message(text="(1) Thông báo đến CĐT về yêu cầu thanh lý HĐMB/TTĐBKKHĐ bằng email, văn bản.")
        dispatcher.utter_message(text="(2) TTDVKH sẽ mời KH đến văn lòng tại tòa nhà Léman - số 117A Nguyễn Đình Chiểu, Quận 3, T.P Hồ Chí Minh để làm việc trực tiếp và hỗ trợ.")
        dispatcher.utter_message(text="(3) Khi thực hiện thủ tục thanh lý, theo điều 2.4 quy định tại Thỏa Thuận Chấm Dứt, khách hàng phải bàn giao lại cho CĐT đầy đủ và chính xác các hồ sơ:")
        dispatcher.utter_message(text="- Bản gốc Phiếu Giữ Chỗ Không Hoàn Lại")
        dispatcher.utter_message(text="- Bản gốc TTĐB ký kết hợp đồng và các phụ lục đính kèm")
        dispatcher.utter_message(text="- Bản gốc các Giấy xác nhận Thông Tin Chuyển tiền (nếu có)")
        dispatcher.utter_message(text="- CMND/ Hộ Chiếu và hộ khẩu của bên B (1 bản sao y chứng thực)")
        dispatcher.utter_message(text="- Các giấy tờ liên quan khác nếu có")
        dispatcher.utter_message(
            text="Thủ tục cho khách hàng là người nước ngoài muốn thanh lý: Tùy từng thời điểm, CĐT sẽ hướng dẫn thủ tục thanh lý theo quy định của PL",
            buttons=[
                {"title": "Hồ sơ thanh lý", "payload": "Hồ sơ thanh lý"},
                {"title": "Thời gian nhận tiền", "payload": "Thời gian nhận tiền sau thanh lý"},
                {"title": "Tư vấn thêm", "payload": "Tư vấn thêm cho mình"}
            ]
        )

        return []

class ActionConnectAndStoreConsultationInfo(Action):

    def name(self) -> Text:
        return "action_store_consultation_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Construct connection string
        # conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}"\
        #     .format(host, user, dbname, password, sslmode)
        # conn = psycopg2.connect(conn_string)
        # print("Connection established")

        # cursor = conn.cursor()

        # # Insert some data into the table
        # cursor.execute("INSERT INTO subscribers (name, email, phone_number) VALUES (%s, %s, %s);", \
        #     (tracker.get_slot("name"), tracker.get_slot("email"), tracker.get_slot("phone_number")))

        # # Clean up
        # conn.commit()
        # cursor.close()
        # conn.close()

        with open('actions/consultation.csv', mode='a') as f:
            writer = csv.writer(f)
            writer.writerow([
                tracker.get_slot("email"),
                tracker.get_slot("phone_number"),
                tracker.get_slot("name")])

        # https://docs.python.org/3/reference/lexical_analysis.html#string-literal-concatenation
        dispatcher.utter_message(
            text=("Cảm ơn Anh/Chị đã để lại thông tin! "
            "{} xin xác nhận lại thông tin của Anh/Chị là:\n"
            "- Họ tên của Anh/Chị là: {}\n"
            "- Số điện thoại: {}\n"
            "- Email: {}\n"
            "Nhân viên dự án sẽ liên hệ và tư vấn cho mình trong thời gian sớm nhất ạ!")\
            .format(
                tracker.get_slot("page_name"),
                tracker.get_slot("name"),
                tracker.get_slot("phone_number"),
                tracker.get_slot("email")))

        return []


class ActionConnectAndStoreSampleHouseVisitorInfo(Action):

    def name(self) -> Text:
        return "action_store_sample_house_visitor_info"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        with open('actions/sample_house_visitor.csv', mode='a') as f:
            writer = csv.writer(f)
            writer.writerow([
                tracker.get_slot("email"),
                tracker.get_slot("phone_number"),
                tracker.get_slot("name"),
                tracker.get_slot("visit_date"),
                tracker.get_slot("visit_time")])

        dispatcher.utter_message(
            text=("Cảm ơn Anh/Chị đã để lại thông tin, "
            "{} xin xác nhận lại thông tin đặt lịch xem nhà mẫu của Anh/chị như sau:\n"
            "- Ngày đăng ký xem: {}\n"
            "- Giờ đăng ký xem: {}\n"
            "- Họ tên của Anh/Chị là: {}\n"
            "- Số điện thoại: {}\n"
            "- Email của Anh/chị là: {}\n"
            "Nhân viên dự án sẽ liên hệ lại để xác nhận lịch xem nhà mẫu của Anh/chị trong thời gian sớm nhất ạ. "
            "Hẹn gặp lại Anh/chị tại dự án!")\
            .format(
                tracker.get_slot("page_name"),
                tracker.get_slot("visit_date"),
                tracker.get_slot("visit_time"),
                tracker.get_slot("name"),
                tracker.get_slot("phone_number"),
                tracker.get_slot("email")))

        return []