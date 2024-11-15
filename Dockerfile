# Use a specific version of the PyTorch image with CUDA and cuDNN support
FROM pytorch/pytorch:2.1.2-cuda11.8-cudnn8-runtime

RUN apt-get update -y && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    # libffi-dev \
    # libwayland-client0 \
    wget \
    vim \
    git \
    curl \
    libsndfile1 \
    fluidsynth \
    libfluidsynth-dev && \
    rm -rf /var/lib/apt/lists/*

# for some reason part of libffi was causing errors; following fixed it 
ENV LD_PRELOAD=/usr/lib/x86_64-linux-gnu/libffi.so.7

WORKDIR /usr/src/work

COPY . .

RUN pip install --no-cache-dir -r requirements.txt \
    -e . \
    jupyter jupyter-core typing_extensions

# To run jupyter in remote development scenario with VSCode
# from https://stackoverflow.com/questions/63998873/vscode-how-to-run-a-jupyter-notebook-in-a-docker-container-over-a-remote-serve
# Add Tini. Tini operates as a process subreaper for jupyter. This prevents kernel crashes.
ENV TINI_VERSION=v0.6.0
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini /usr/bin/tini
RUN chmod +x /usr/bin/tini

RUN rm -rf /usr/src/work

WORKDIR /usr/src/app

EXPOSE 8888

# Use Tini as the container's entry point
ENTRYPOINT ["/usr/bin/tini", "--"]

# Start Jupyter Notebook
CMD ["jupyter", "notebook", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root", "--NotebookApp.token=''", "--NotebookApp.password=''"]
