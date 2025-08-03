# decoder.py
import os
import subprocess


def find_ncm_files(folder):
    ncm_files = []
    for root, _, files in os.walk(folder):
        for file in files:
            if file.lower().endswith(".ncm"):
                ncm_files.append(os.path.join(root, file))
    return ncm_files


if __name__ == "__main__":
    # 修改为你本机网易云下载目录
    ncm_folder = r"D:\CloudMusic\VipSongsDownload"

    # 转换输出目录：桌面
    out_folder = os.path.join(os.path.expanduser("~"), "Desktop")

    files = find_ncm_files(ncm_folder)
    print(f"检测到 {len(files)} 个 .ncm 文件，准备转换...")

    for idx, ncm_file in enumerate(files, 1):
        print(f"[{idx}/{len(files)}] 正在转换：{ncm_file}")
        cmd = ["ncmdump", ncm_file, "-o", out_folder]
        try:
            subprocess.run(cmd, check=True)
        except Exception as e:
            print(f"转换失败: {ncm_file}\n原因: {e}")

    print(f"\n✅ 全部转换完成！输出目录：{out_folder}")
