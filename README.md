# Chiến tranh chống Mỹ - Trò chơi Xe tăng

Trò chơi chiến đấu xe tăng tái hiện các sự kiện lịch sử quan trọng trong cuộc chiến tranh Việt Nam (1955-1975). Người chơi điều khiển xe tăng Việt Nam qua các trận chiến lịch sử dẫn đến sự thống nhất đất nước.

![Hình ảnh trò chơi](assets/images/main_menu_img.png)

## Động lực Phát triển

Trò chơi này được tạo ra với niềm đam mê và mong muốn mang đến một phương tiện giải trí độc đáo, nơi người chơi không chỉ được thư giãn với những trận đấu xe tăng kịch tính mà còn có cơ hội sống lại những trang sử hào hùng của dân tộc. Chúng mình tin rằng, việc lồng ghép kiến thức lịch sử vào một trò chơi tương tác sẽ giúp mọi người, đặc biệt là thế hệ trẻ, tiếp cận và ghi nhớ các sự kiện quan trọng một cách tự nhiên và hứng khởi hơn. Mục tiêu của chúng mình là tạo ra một trải nghiệm "học mà chơi, chơi mà học", khơi gợi niềm tự hào dân tộc và sự trân trọng đối với những hy sinh xương máu của cha ông để có được hòa bình, thống nhất ngày nay. Hãy cùng chúng mình khám phá lịch sử qua từng màn chơi và cảm nhận khí thế chiến đấu bất khuất của quân và dân ta!

## Tính năng

- 5 màn chơi tiến triển dựa trên các trận chiến lịch sử
- Video clip và hình ảnh lịch sử giữa các màn chơi
- Cơ chế chiến đấu xe tăng với hệ thống bắn súng
- Độ khó tăng dần qua từng màn chơi
- Giao diện tiếng Việt hoàn toàn
- Chuỗi chiến thắng thể hiện quá trình thống nhất Việt Nam

## Yêu cầu hệ thống

- Python 3.6 trở lên
- pygame
- moviepy

## Cài đặt

1. Clone repository này:
```
git clone https://github.com/tranminhvu945/Game_KNNN.git
```

2. Cài đặt các gói yêu cầu:
```
pip install -r requirements.txt
```

## Cách chơi

1. Chạy trò chơi:
```
python main.py
```

2. Điều khiển:
   - Phím mũi tên: Di chuyển xe tăng
   - Phím cách: Bắn
   - P: Tạm dừng trò chơi
   - ESC: Thoát trò chơi

3. Lối chơi:
   - Tiêu diệt tất cả xe tăng địch để tiến đến màn chơi tiếp theo
   - Tránh đạn địch để duy trì lực lượng
   - Hoàn thành 5 màn chơi để chiến thắng

## Các màn chơi

1. **Điện Biên Phủ (1954)** - Trận chiến quyết định kết thúc thời kỳ thực dân Pháp
2. **Vĩ tuyến 17 (1954-1960s)** - Sự phân chia Việt Nam tại vĩ tuyến 17
3. **Tết Mậu Thân (1968)** - Cuộc tổng tấn công của quân đội Miền Bắc
4. **Chiến dịch Quảng Trị (1972)** - Trận chiến quan trọng trong Chiến dịch Xuân Hè
5. **Giải phóng Sài Gòn (30/4/1975)** - Trận chiến cuối cùng dẫn đến thống nhất đất nước

## Cấu trúc dự án

- main.py - Điểm khởi đầu của trò chơi
- src - Mã nguồn trò chơi chính
  - `game.py` - Vòng lặp trò chơi chính và khởi tạo
  - `entities/` - Các đối tượng trong trò chơi (anh hùng, kẻ địch, đạn, v.v.)
  - `systems/` - Các hệ thống trò chơi (va chạm, quản lý màn chơi, sinh sản)
  - `configs/` - Cấu hình và hằng số trò chơi
  - `helpers/` - Các chức năng tiện ích
- ui - Các thành phần giao diện người dùng
  - `screen/` - Màn hình trò chơi (menu chính, tạm dừng, kết thúc, v.v.)
  - `hud.py` - Hiển thị thông tin trong quá trình chơi
- assets - Tài nguyên trò chơi (hình ảnh, video, font chữ)